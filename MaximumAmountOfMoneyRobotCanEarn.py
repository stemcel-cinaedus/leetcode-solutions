class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        monies = 0
        n, m = len(coins), len(coins[0])
        g = [[[-10**9] * 3 for _ in range(m)] for _ in range(n)]

        g[0][0][1] = g[0][0][2] = 0
        g[0][0][0] = coins[0][0]

        for a in range(n):
            for b in range(m):
                for c in range(3):
                    if a:
                        g[a][b][c] = max(g[a][b][c], g[a-1][b][c] + coins[a][b])
                    if a and c:
                         g[a][b][c] = max(g[a][b][c], g[a-1][b][c-1])
                    if b:
                         g[a][b][c] = max(g[a][b][c], g[a][b-1][c] + coins[a][b])
                    if b and c:
                         g[a][b][c] = max(g[a][b][c], g[a][b-1][c-1])
                    
        return max(g[n-1][m-1])