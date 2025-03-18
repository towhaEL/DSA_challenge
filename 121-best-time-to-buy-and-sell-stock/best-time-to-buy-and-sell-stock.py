class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        p = 0

        st = prices[0]
        for i in range(len(prices)-1):
            if prices[i+1]<st:
                st = prices[i+1]
                continue
            p = prices[i+1] - st
            mp = max(mp, p)

        return mp    
