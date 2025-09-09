class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # Day 1: first person knows
        
        for i in range(1, n + 1):
            for j in range(i + delay, min(n + 1, i + forget)):
                dp[j] = (dp[j] + dp[i]) % MOD
        
        # Sum people who still remember on day n
        return sum(dp[max(1, n - forget + 1): n + 1]) % MOD
