class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(',
                 '}':'{',
                 ']':'[',
        }
        q = []
        for v in s:
            if v in "])}":
                if not q or q.pop() != m[v]:
                    return False
            else:
                q.append(v)
        return True if not q else False