class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {}
        for move in moves:
            if directions.get(move):
                directions[move] += 1
            else:
                directions[move] = 1
        if directions.get("U") == directions.get("D") and directions.get("L") == directions.get("R"):
            return True
        else:
            return False
