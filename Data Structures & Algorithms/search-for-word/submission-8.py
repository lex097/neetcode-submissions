class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ret = False
        seen = set()

        def backtrack(r, c, index):
            if index == len(word):
                self.ret = True
                return     
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (board[r][c] != word[index]) or (r, c) in seen):
                return 

            seen.add((r, c))
            backtrack(r+1, c, index + 1)
            backtrack(r-1, c, index + 1)
            backtrack(r, c+1, index + 1)
            backtrack(r, c-1, index + 1)
            seen.remove((r, c))
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, 0)
        return self.ret