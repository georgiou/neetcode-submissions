class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n - 1
        area = 0
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax, height[l])
                area += lmax-height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                area += rmax-height[r]
        return area
            
