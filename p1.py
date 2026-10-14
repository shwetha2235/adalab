from typing import List

# Function to search for an element
def search(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# Function to calculate power
def myPow(x: float, n: int) -> float:
    result = 1.0
    power = abs(n)

    while power > 0:
        if power % 2 == 1:
            result *= x
        x *= x
        power //= 2

    if n < 0:
        result = 1.0 / result

    return result


# Main program
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target element: "))

index = search(nums, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")

x = float(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Power result:", myPow(x, n))
