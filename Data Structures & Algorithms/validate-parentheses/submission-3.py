class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(',
                 '}':'{',
                 ']':'[',
        }
        q = []
        for v in s:
            if v in "[({":
                q.append(v)
            elif v in "])}":
                if not q or q.pop() != m[v]:
                    return False
            else:
                return False
        if q:
            return False
        return True