class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff = 0
        mn = prices[0]
        mx = prices[0]

        for i in range(1,n):
            v = prices[i]
            if v < mn:
                mn = v
                mx = 0

            mx = max(mx,v)
            diff = max(diff, mx-mn)
        return diff

            