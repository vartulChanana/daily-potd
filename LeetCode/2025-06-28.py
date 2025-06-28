from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        k_largest = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        k_largest.sort(key=lambda x: x[1])
        return [num for num, _ in k_largest]
