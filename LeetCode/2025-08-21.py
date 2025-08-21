from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            # Update heights (like histogram)
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            # Count submatrices ending at this row
            stack = []
            sum_row = 0
            for j in range(n):
                count = 1
                while stack and stack[-1][0] >= heights[j]:
                    h, c = stack.pop()
                    sum_row -= h * c
                    count += c
                sum_row += heights[j] * count
                stack.append((heights[j], count))
                total += sum_row
        
        return total
