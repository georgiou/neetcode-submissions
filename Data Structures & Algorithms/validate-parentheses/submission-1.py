class Solution:
    def isValid(self, s: str) -> bool:
       stack = deque()
       pairs = {"]": "[", ")":"(", "}":"{"}
       for i in s:
        if i in "[({":
            stack.append(i)
        else:
            if not stack:
                return False
            m = stack.pop()
            if pairs[i] != m:
                return False
       if stack:
         return False
       return True