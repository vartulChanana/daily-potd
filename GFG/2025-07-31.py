class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict

        diff = defaultdict(int)

        for start, end in intervals:
            diff[start] += 1
            diff[end + 1] -= 1  

        active = 0
        prev = None
        max_powerful = -1

        for point in sorted(diff):
            if prev is not None and active >= k:
                max_powerful = max(max_powerful, point - 1) 
            active += diff[point]
            prev = point

        return max_powerful
