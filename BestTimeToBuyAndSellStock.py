class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_s=float('inf')
        max_p=0

        for price in prices:
            if price<min_s:
                min_s=price
            else:
                max_p=max(max_p,price-min_s)
        return max_p