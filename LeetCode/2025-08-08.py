class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0  # For large n, probability is ~1

        from functools import lru_cache

        @lru_cache(None)
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25 * (
                dfs(a - 4, b) +
                dfs(a - 3, b - 1) +
                dfs(a - 2, b - 2) +
                dfs(a - 1, b - 3)
            )

        # Scale n down to reduce problem size
        n = (n + 24) // 25  # Round up to nearest multiple of 25
        return dfs(n, n)
