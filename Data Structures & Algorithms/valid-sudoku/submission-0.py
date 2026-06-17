class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or len(board[0]) != 9:
            return False
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                box = (i // 3, j // 3, val)
                row = (i, val)
                col = (val, j)
                if box in seen or row in seen or col in seen:
                    return False
                seen.update([box, row, col])
        return True

