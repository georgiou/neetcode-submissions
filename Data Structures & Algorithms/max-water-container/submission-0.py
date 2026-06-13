class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        n = len(heights)

        l, r = 0, n-1
        while l<r:
            lh = heights[l]
            rh = heights[r]
            width = r - l
            if lh > rh:
                r -= 1
                height = rh
            else:
                l += 1
                height = lh
            maxvol = max(maxvol, height*width)
        return maxvol
            