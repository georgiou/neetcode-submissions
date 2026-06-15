class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        rmax = [0] * n
        lmax = [0] * n

        lmax[0]=height[0]
        rmax[n-1]=height[n-1]
        for i in range(1,n-1):
            lmax[i]=max(lmax[i-1], height[i])
            irev = n-1-i
            rmax[irev]=max(rmax[irev+1], height[irev])

        area=0
        for i in range(1,n-1):
            area += max(0, min(lmax[i-1], rmax[i+1]) - height[i])
        return area
            
