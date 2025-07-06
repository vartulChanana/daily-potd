from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        self.freq2[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.freq2.get(complement, 0)
        return result

