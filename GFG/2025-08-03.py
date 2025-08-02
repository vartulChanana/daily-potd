class Solution:
    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])
        
        # Step 1: Create a difference matrix
        diff = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # Step 2: Apply each operation to diff matrix
        for v, r1, c1, r2, c2 in opr:
            diff[r1][c1] += v
            if c2 + 1 < m:
                diff[r1][c2 + 1] -= v
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= v
            if r2 + 1 < n and c2 + 1 < m:
                diff[r2 + 1][c2 + 1] += v

        # Step 3: Convert diff matrix to actual updates via prefix sums
        for i in range(n):
            for j in range(1, m):
                diff[i][j] += diff[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Step 4: Add diff matrix to original mat
        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]

        return mat
