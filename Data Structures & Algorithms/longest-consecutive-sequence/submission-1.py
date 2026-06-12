class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq=0
        seen = set(nums)
        for i in seen:
            if i-1 not in seen:
                current_max=1
                while i+current_max in seen:
                    current_max+=1
                max_seq=max(max_seq, current_max)
        return max_seq


