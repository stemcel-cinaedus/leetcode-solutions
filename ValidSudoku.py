class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i, j = 0, 0
        for y in board:
            el = set()
            for x in y:
                if x in el and x != ".":
                    return False
                else:
                    el.add(x)
        
        while i < len(board):
            j = 0
            seen = set()
            while j < len(board):
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                else:
                    seen.add(board[j][i])
                j += 1
            i += 1

        sub = [0,0]
        while sub[1] < 3:
            s = set()
            for r in range((sub[0] * 3), (3 + (sub[0]) * 3)):
                for c in range((sub[1] * 3), (3 + (sub[1] * 3))):
                    if board[r][c] != "." and board[r][c] in s:
                        return False
                    else:
                        s.add(board[r][c])
            if sub[0] < 2:
                sub[0] += 1
                s.clear()
            else:
                sub[0] = 0
                sub[1] += 1
                s.clear()
        return True
