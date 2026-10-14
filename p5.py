
from typing import List
from dataclasses import dataclass


# Fractional Knapsack
def fractional_knapsack(
    weights: List[int],
    values: List[int],
    capacity: int
) -> float:

    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal length")

    if capacity < 0 or any(w <= 0 for w in weights):
        raise ValueError("Invalid weight or capacity")

    items = sorted(
        zip(weights, values),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    profit = 0.0

    for weight, value in items:
        if capacity == 0:
            break

        take = min(weight, capacity)
        profit += take * (value / weight)
        capacity -= take

    return profit


# Job Scheduling
@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    jobs = sorted(jobs, key=lambda job: job.profit, reverse=True)

    max_deadline = max(
        (job.deadline for job in jobs), default=0
    )
    slots = [None] * max_deadline

    for job in jobs:
        if job.profit <= 0:
            continue

        for slot in range(min(job.deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job.id
                break

    return [job_id for job_id in slots if job_id is not None]


# Main program
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Knapsack Profit:",
      fractional_knapsack(weights, values, capacity))

jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)
print("Optimal Job Sequence:", sequence)
