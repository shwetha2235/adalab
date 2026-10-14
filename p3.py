
from typing import List, Tuple

def findKthLargest(nums: List[int], k: int) -> int:
    if not nums or k < 1 or k > len(nums):
        raise ValueError("Invalid array or k value")

    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k - 1]


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    if not nums:
        raise ValueError("Array cannot be empty")

    return min(nums), max(nums)


# Main program
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k value: "))

print("Kth largest element:", findKthLargest(nums, k))

minimum, maximum = findMinMax(nums)
print("Minimum element:", minimum)
print("Maximum element:", maximum)
print("Min-Max pair:", (minimum, maximum))
