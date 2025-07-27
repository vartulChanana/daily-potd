class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])

        first_row_has_zero = any(mat[0][j] == 0 for j in range(m))
        first_col_has_zero = any(mat[i][0] == 0 for i in range(n))

        # Mark zeros on first row and column
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Set zeroes based on flags in first row and column
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(m):
                mat[0][j] = 0

        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(n):
                mat[i][0] = 0
