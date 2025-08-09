class Solution:
    def getLongestPrefix(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return -1

        # Build Z-array
        Z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1

        # Find the largest proper prefix length L with Z[L] >= n - L
        for L in range(n - 1, 0, -1):
            if Z[L] >= n - L:
                return L
        return -1
