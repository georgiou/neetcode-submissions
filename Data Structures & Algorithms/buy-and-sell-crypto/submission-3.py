class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mx = 0

        while r < len(prices):
            pl = prices[l]
            pr = prices[r]

            if pl < pr:
                mx = max(mx, pr - pl)
            else:
                l = r
            r+=1
        return mx 