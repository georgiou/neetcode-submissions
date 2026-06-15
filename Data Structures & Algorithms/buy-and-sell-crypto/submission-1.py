class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        mn = float('inf')

        for v in prices:
            if v < mn:
                mn = v
            elif v -mn > diff:
                diff = v - mn
        return diff

            