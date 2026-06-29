class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False

        freq1 = [0]*26
        freq2 = [0]*26

        for c in s1:
            freq1[ord(c)-ord('a')] += 1
        
        slow = 0
        size = 0
        for c in s2:
            freq2[ord(c)-ord('a')] += 1
            size += 1

            if size < n1:
                next
            elif size > n1:
                freq2[ord(s2[slow])-ord('a')] -= 1
                slow += 1
                size -= 1
            if freq2 == freq1:
                return True
        return False