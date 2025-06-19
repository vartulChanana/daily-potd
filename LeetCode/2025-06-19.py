from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        subsequences_count = 0
        n = len(nums)
        i = 0
        
        while i < n:
            subsequences_count += 1
            start = nums[i]
            
            while i < n and nums[i] - start <= k:
                i += 1
        
        return subsequences_count
