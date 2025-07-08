from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        start_days = [e[0] for e in events]

        @lru_cache(None)
        def dp(index, remaining):
            if index == n or remaining == 0:
                return 0
            next_index = bisect_right(start_days, events[index][1])
            skip = dp(index + 1, remaining)
            take = events[index][2] + dp(next_index, remaining - 1)
            return max(skip, take)

        return dp(0, k)
