from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(r, c, ch):
            # Check row
            for i in range(9):
                if board[r][i] == ch:
                    return False

            # Check column
            for i in range(9):
                if board[i][c] == ch:
                    return False

            # Check 3x3 sub-box
            start_r, start_c = 3 * (r // 3), 3 * (c // 3)
            for i in range(start_r, start_r + 3):
                for j in range(start_c, start_c + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for ch in map(str, range(1, 10)):
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                if backtrack():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        backtrack()
