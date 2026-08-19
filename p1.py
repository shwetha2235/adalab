# Program 1: Implement search(nums: List[int], target: int) -> int and myPow(x: float, n: int)-> float functions taking an integer array/target and base/exponent pairs, returning index and computed value respectively.
# Binary Search
# Searches for target in a sorted array and returns its index.
# Time Complexity: O(log n)
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (right-left)//2 + left

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return -1

# Exponentiation by Squaring
# Calculates x raised to the power n efficiently.
# Time Complexity: O(log n)
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n < 0:
        n = -n
        return 1 / myPow(x, n)

    half = myPow(x, n // 2)

    if n%2 == 0:
        return half * half
    else:
        return half * half * x

# Test cases
print(search([-1, 0, 3, 5, 9, 12], 9))
print(myPow(2, 5))
print(myPow(2, -3))