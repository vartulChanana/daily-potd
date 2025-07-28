class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        
        row_sum = [0] * n
        col_sum = [0] * n
        
        for i in range(n):
            for j in range(n):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]
        
        max_sum = max(max(row_sum), max(col_sum))
        total_ops = 0
        
        i = 0
        j = 0
        
        while i < n and j < n:
            diff = min(max_sum - row_sum[i], max_sum - col_sum[j])
            mat[i][j] += diff
            row_sum[i] += diff
            col_sum[j] += diff
            total_ops += diff
            
            if row_sum[i] == max_sum:
                i += 1
            if col_sum[j] == max_sum:
                j += 1
                
        return total_ops

