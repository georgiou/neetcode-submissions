class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers: List[int], target: int) -> List[int]:
            n = len(numbers)
            left = 0
            right = n-1
            ans = []
            while left < right:
                if left > 0 and numbers[left]==numbers[left-1]:
                    left += 1
                    continue

                s = numbers[left] + numbers[right]
                if s == target:
                    ans.append([numbers[left], numbers[right]])
                    left +=1
                elif s > target:
                    right -= 1
                else :
                    left += 1
            return ans

        ans = []
        nums = sorted(nums)
        for  i in range(len(nums)-1):
            target = -nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue
            ts = twoSum(nums[i+1:], target)
            for v1,v2 in ts:
                ans.append([nums[i], v1, v2])
        return ans