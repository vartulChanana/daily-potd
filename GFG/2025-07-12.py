class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)
        m = len(mat[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = mat[i][0]

        for j in range(1, m):
            for i in range(n)
                left = dp[i][j - 1]
                left_up = dp[i - 1][j - 1] if i > 0 else 0
                left_down = dp[i + 1][j - 1] if i < n - 1 else 0

                dp[i][j] = mat[i][j] + max(left, left_up, left_down)
              
        max_gold = max(dp[i][m - 1] for i in range(n))
        return max_gold

