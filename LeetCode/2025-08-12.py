class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: generate all powers <= n
        powers = []
        i = 1
        while (p := i ** x) <= n:
            powers.append(p)
            i += 1
        
        # Step 2: 1D DP array
        dp = [0] * (n + 1)
        dp[0] = 1  # one way to make sum 0 (empty set)
        
        # Step 3: process each power
        for power in powers:
            for t in range(n, power - 1, -1):
                dp[t] = (dp[t] + dp[t - power]) % MOD
        
        return dp[n]
