import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []

        for i, n in enumerate(nums):
            left = i - k
            heapq.heappush(heap, (-n, -i))
            if i >= k - 1:
                while len(heap) > k and -heap[0][1] <= left:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result