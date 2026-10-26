from typing import List
import random


# KMP String Matching
def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    lps = [0] * len(needle)
    j = 0

    for i in range(1, len(needle)):
        while j > 0 and needle[i] != needle[j]:
            j = lps[j - 1]
        if needle[i] == needle[j]:
            j += 1
            lps[i] = j

    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = lps[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1

    return -1


# Randomized Stream Sampling
class Randomizer:
    def __init__(self, stream: List[int]):
        self.stream = stream
        self.sample = None

    def getRandom(self) -> int:
        for i, item in enumerate(self.stream, 1):
            if random.randrange(i) == 0:
                self.sample = item
        return self.sample


# Examples
print("Pattern index:", strStr("hello", "ll"))

r = Randomizer([10, 20, 30, 40, 50])
print("Random sample:", r.getRandom())