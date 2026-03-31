class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for y, x in walls:
            matrix[y][x] = 1
        for y, x in guards:
            matrix[y][x] = 1
        for y, x in guards:
            l, r = x-1, x+1
            while l >= 0:
                if matrix[y][l] == 0:
                    matrix[y][l] = 2
                elif matrix[y][l] == 1:
                    break
                l -= 1
            while r <= n - 1:
                if matrix[y][r] == 0:
                    matrix[y][r] = 2
                elif matrix[y][r] == 1:
                    break
                r += 1
            d, u = y + 1, y - 1
            while u >= 0:
                if matrix[u][x] == 0:
                    matrix[u][x] = 2
                elif matrix[u][x] == 1:
                    break
                u -= 1
            while d <= m - 1:
                if matrix[d][x] == 0:
                    matrix[d][x] = 2
                elif matrix[d][x] == 1:
                    break
                d += 1
        
        return sum(r.count(0) for r in matrix)
