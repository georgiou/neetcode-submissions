from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        left = 0
        right = 0

        tset = Counter(t)
        sset = Counter()

        minres = ""

        while right <= ns:
            if tset <= sset:
                sset.subtract(s[left])
                if minres == "" or right-left < len(minres):
                    minres = s[left:right]
                left += 1
            else:
                if right < ns:
                    sset.update(s[right])
                    right += 1
                else:
                    return minres