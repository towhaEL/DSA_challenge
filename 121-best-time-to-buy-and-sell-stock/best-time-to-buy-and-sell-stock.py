class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = float('inf')

        for st in prices:
            if st < buy:
                buy = st

            profit = st - buy
            maxProfit = max(profit, maxProfit)

        return maxProfit