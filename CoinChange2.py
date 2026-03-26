class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        t = [1] + [0] * amount
        for c in coins:
            for x in range(c, amount+1):
                t[x] += t[x-c]
        return t[amount]
