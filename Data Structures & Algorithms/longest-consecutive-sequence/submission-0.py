class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq=0
        seen = {}
        for i in nums:
            seen[i]=True
        for i in seen:
            if i-1 not in seen:
                current_max=1
                start=i+1
                while start in seen:
                    current_max+=1
                    start +=1
                max_seq=max(max_seq, current_max)
        return max_seq


