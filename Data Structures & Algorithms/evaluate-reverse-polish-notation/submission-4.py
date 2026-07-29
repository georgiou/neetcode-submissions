class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == '+':
                s.append(s.pop() + s.pop())
            elif token == '-':
                s.append(- s.pop() + s.pop())
            elif token == '*':
                s.append(s.pop() * s.pop())
            elif token == '/':
                tmp = s.pop()
                s.append(int(s.pop()/tmp))
            else:
                s.append(int(token))
        return s[0]
