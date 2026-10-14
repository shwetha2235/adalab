
from typing import List

class Sort:

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        return (self.quick_sort(left) + [pivot]
                + self.quick_sort(right))


# Main program
s = Sort()

arr = list(map(int, input("Enter array elements: ").split()))

print("Merge Sort:", s.merge_sort(arr))
print("Quick Sort:", s.quick_sort(arr))
