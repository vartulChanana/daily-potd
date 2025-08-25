class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = {}

        # Step 1: Collect elements in diagonals
        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        result = []

        # Step 2: Traverse diagonals
        for s in range(m + n - 1):
            if s % 2 == 0:  # even sum → reverse order
                result.extend(reversed(diagonals[s]))
            else:  # odd sum → normal order
                result.extend(diagonals[s])

        return result
