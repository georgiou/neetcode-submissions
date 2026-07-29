class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        n = len(self.s)
        if not self.m or (self.s and val <= self.s[self.m[-1]]):
            self.m.append(n)
        self.s.append(val)

    def pop(self) -> None:
        n = len(self.s)
        while len(self.m)>1 and self.m[-1] >= n-1:
            self.m.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s[self.m[-1]]