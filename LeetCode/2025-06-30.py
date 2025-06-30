from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_length = 0
        
        for num in frequency:
            if num + 1 in frequency:
                current_length = frequency[num] + frequency[num + 1]
                max_length = max(max_length, current_length)
        
        return max_length
