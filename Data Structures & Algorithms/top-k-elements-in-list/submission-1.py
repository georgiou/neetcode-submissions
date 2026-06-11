from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freq = [[] for _ in range(len(nums)+1)]
        for f,v in counts.items():
            freq[v].append(f)

        ans=[]
        for a in reversed(freq):
            for v in a:
              ans.append(v)
              if len(ans) >= k:
                 return ans

        return ans