from typing import List
import math

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # helper: total base-4 digit counts from 1 to n
        def prefix_sum(n: int) -> int:
            if n <= 0:
                return 0
            res = 0
            length = 1
            start = 1
            while start <= n:
                end = min(n, 4**length - 1)
                res += (end - start + 1) * length
                start = 4**length
                length += 1
            return res
        
        total = 0
        for l, r in queries:
            s = prefix_sum(r) - prefix_sum(l - 1)
            total += (s + 1) // 2   # ceil(s/2)
        return total
