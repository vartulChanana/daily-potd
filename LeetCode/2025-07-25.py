from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        positive_sum = sum(num for num in unique_nums if num > 0)
        
        if positive_sum == 0:
            return max(nums)
        
        return positive_sum
