#dfs from border Os
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        keepAsO = set()
        def search(r, c):
            if (r >= len(board)) or (c >= len(board[0])) or (r < 0) or (c < 0) or ((r, c) in keepAsO) or (board[r][c] == "X"):
                return
            keepAsO.add((r, c))

            search(r + 1, c)
            search(r - 1, c)
            search(r, c + 1)
            search(r, c - 1)
            return
        for r in range(len(board)):
            search(r, 0)
            search(r, len(board[0]) - 1)
        for c in range(len(board[0])):
            search(0, c)
            search(len(board) - 1, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) in keepAsO:
                    continue
                board[r][c] = "X"
        