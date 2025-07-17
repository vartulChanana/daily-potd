from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        dp = defaultdict(int)
        max_len = 1
        
        for i in range(n):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                # Extend any sequence ending at j with same mod
                dp[(i, mod)] = max(dp[(i, mod)], dp[(j, mod)] + 1)
                max_len = max(max_len, dp[(i, mod)])
        
        return max_len + 1  # +1 to count the first element of the subsequence
