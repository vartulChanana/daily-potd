class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        max_sum = float('-inf')

        for left in range(m):
            temp = [0] * n  # Temporary 1D array to store sum of rows between two columns
            for right in range(left, m):
                # Update each row sum from left to right column
                for i in range(n):
                    temp[i] += mat[i][right]
                
                # Apply Kadane's Algorithm on temp
                curr_sum = temp[0]
                max_curr = temp[0]
                for i in range(1, n):
                    curr_sum = max(temp[i], curr_sum + temp[i])
                    max_curr = max(max_curr, curr_sum)
                
                # Update global max sum
                max_sum = max(max_sum, max_curr)

        return max_sum
