# Rate Monotonic Scheduling Simulation

This project implements a task scheduling algorithm using Rate Monotonic Scheduling (RMS). The goal is to determine if a set of periodic tasks is schedulable based on their computation times and periods, and to find the optimal schedule if they are.

## Usage

1. Prepare a JSON file with the task specifications (see the [Input Format](#input-format) section).

2. Run the script with the JSON file as an argument:
    ```sh
    python script.py <input_file>
    ```

## Input Format

The input JSON file should contain an array of tasks, where each task is an object with `id`, `execution_time`, and `period` fields. Here is an example:

```json
[
    {
        "id": 1,
        "execution_time": 2,
        "period": 6
    },
    {
        "id": 2,
        "execution_time": 2,
        "period": 8
    },
    {
        "id": 3,
        "execution_time": 2,
        "period": 12
    }
]
```
## Output Example
```
The task set is schedulable under the Liu and Layland criterion.
Hyperperiod: 24

Time | Task
------------
   0 | 1
   1 | 1
   2 | 2
   3 | 2
   4 | 3
   5 | 3
   6 | 1
   7 | 1
   8 | 2
   9 | 2
  10 | Idle
  11 | Idle
  12 | 1
  13 | 1
  14 | 3
  15 | 3
  16 | 2
  17 | 2
  18 | 1
  19 | 1
  20 | Idle
  21 | Idle
  22 | Idle
  23 | Idle
```
