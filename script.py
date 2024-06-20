import json
import numpy as np
import sys

# Task structure
class Task:
    def __init__(self, id, computation_time, period):
        self.id = id
        self.computation_time = computation_time
        self.period = period
        self.remaining_time = computation_time
        self.next_deadline = period

# Function to simulate the Rate Monotonic Scheduling
def rate_monotonic_scheduling(tasks, hyperperiod):
    time = 0
    schedule = []
    deadline_missed = False

    while time < hyperperiod:
        # Sort tasks by period (Rate Monotonic)
        tasks.sort(key=lambda x: x.period)
        
        # Check for task deadlines and reset if necessary
        for task in tasks:
            if time == task.next_deadline:
                if task.remaining_time > 0:
                    print(f"Task {task.id} missed its deadline at time {time}")
                    deadline_missed = True
                task.remaining_time = task.computation_time
                task.next_deadline += task.period

        # Select the highest priority task that is ready to run
        for task in tasks:
            if task.remaining_time > 0:
                schedule.append((time, task.id))
                task.remaining_time -= 1
                break
        else:
            # Idle time if no task is ready
            schedule.append((time, "Idle"))

        time += 1

    return schedule, deadline_missed

# Function to calculate hyperperiod (LCM of all task periods)
def calculate_hyperperiod(tasks):
    periods = np.array([task.period for task in tasks])
    return np.lcm.reduce(periods)

# Function to check if the task set is schedulable using Liu and Layland criterion
def is_schedulable(tasks):
    n = len(tasks)
    utilization = sum(task.computation_time / task.period for task in tasks)
    bound = n * (2**(1/n) - 1)
    return utilization <= bound

# Function to perform a full schedulability test by simulating the scheduling
def full_schedulability_test(tasks):
    # Calculate hyperperiod
    hyperperiod = calculate_hyperperiod(tasks)
    print(f"Hyperperiod: {hyperperiod}")

    # Run the RMS algorithm
    schedule, deadline_missed = rate_monotonic_scheduling(tasks, hyperperiod)

    if deadline_missed:
        print("One or more tasks missed their deadlines.")
        return False, schedule
    else:
        return True, schedule

# Main function to read input file and perform schedulability test
def main(input_file):
    tasks = []
    with open(input_file) as f:
        json_data = json.load(f)
    for i in json_data:
        tasks.append(Task(i["id"], i["execution_time"], i["period"]))

    # Check if the task set is schedulable using Liu and Layland criterion
    if is_schedulable(tasks):
        print("The task set is schedulable under the Liu and Layland criterion.")
        # Perform full schedulability test and show schedule
        schedulable, schedule = full_schedulability_test(tasks)
        if schedulable:
            print("\nTime | Task")
            print("------------")
            for time, task_id in schedule:
                print(f"{time:4d} | {task_id}")
    else:
        print("The task set is not schedulable under the Liu and Layland criterion. Performing full schedulability test...")
        schedulable, schedule = full_schedulability_test(tasks)
        if schedulable:
            print("The task set is schedulable based on the full schedulability test.")
            print("\nTime | Task")
            print("------------")
            for time, task_id in schedule:
                print(f"{time:4d} | {task_id}")
        else:
            print("The task set is not schedulable based on the full schedulability test.")

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    main(input_file)
