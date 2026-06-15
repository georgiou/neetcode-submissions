class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        l, r = 0, 1

        mx = 1
        
        seen = set()
        seen.add(s[l])

        while r < n:
            if s[r] not in seen:
                mx = max(mx, r-l+1)
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
        return mx
