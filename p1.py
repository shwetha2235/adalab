from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Searches for target in a sorted array using binary search.
    Returns the index if found, otherwise returns -1.
    """

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def myPow(x: float, n: int) -> float:
    """
    Computes x raised to the power n using fast exponentiation.
    """

    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result = result * x

        x = x * x
        n = n // 2

    return result


def main():
    print("----- Binary Search -----")

    nums = list(map(int, input("Enter sorted array elements: ").split()))
    target = int(input("Enter target element: "))

    index = search(nums, target)

    if index != -1:
        print("Target found at index:", index)
    else:
        print("Target not found")


    print("\n----- Power Function -----")

    x = float(input("Enter base: "))
    n = int(input("Enter exponent: "))

    result = myPow(x, n)

    print("Computed value:", result)


if __name__ == "__main__":
    main()