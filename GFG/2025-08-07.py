class Solution:
    def minDifference(self, arr):
        def to_seconds(t):
            h, m, s = map(int, t.split(':'))
            return h * 3600 + m * 60 + s

        seconds = sorted(to_seconds(t) for t in arr)
        min_diff = float('inf')
        
        for i in range(1, len(seconds)):
            min_diff = min(min_diff, seconds[i] - seconds[i-1])
        
        # Wrap-around difference (last and first)
        circular_diff = 86400 - (seconds[-1] - seconds[0])
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
