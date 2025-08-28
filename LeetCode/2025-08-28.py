from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: Collect elements by diagonal key (i - j)
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Step 2: Sort diagonals
        for key in diagonals:
            if key >= 0:  # bottom-left including main diagonal
                diagonals[key].sort(reverse=True)
            else:  # top-right
                diagonals[key].sort()

        # Step 3: Place back sorted elements
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid
