class Solution:
    def getCount(self, n):
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }
        
        dp = [[0] * 10 for _ in range(n + 1)]
        
        for j in range(10):
            dp[1][j] = 1
        
        for i in range(2, n + 1):
            for j in range(10):
                for move in moves[j]:
                    dp[i][j] += dp[i - 1][move]
        
        total_count = sum(dp[n][j] for j in range(10))
        return total_count
