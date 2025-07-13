class Solution:
    def cuts(self, s: str) -> int:
        n = len(s)
        powers_of_5 = set()
        power = 1
        while power < (1 << n):
            powers_of_5.add(bin(power)[2:])
            power *= 5

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub in powers_of_5 and sub[0] != '0':
                    dp[i] = min(dp[i], dp[j] + 1)

        return -1 if dp[n] == float('inf') else dp[n]
