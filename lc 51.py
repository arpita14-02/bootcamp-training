class Solution:
    def solveNQueens(self, n):
        ans = []

        def safe(row, col, board):
            for r in range(row):
                c = board[r].index("Q")

                # Same column
                if c == col:
                    return False

                # Same diagonal
                if abs(row - r) == abs(col - c):
                    return False

            return True

        def backtrack(row, board):
            if row == n:
                ans.append(board.copy())
                return

            for col in range(n):
                if safe(row, col, board):
                    board.append("." * col + "Q" + "." * (n - col - 1))
                    backtrack(row + 1, board)
                    board.pop()

        backtrack(0, [])
        return ans


# For VS Code
n = 4
obj = Solution()
print(obj.solveNQueens(n))