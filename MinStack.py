class MinStack:

    def __init__(self):
        self.s = list()
        self.n = -1
        self.s_min = list()
    def push(self, val: int) -> None:
        if self.n < 0:
            self.s_min.append(val) 
        elif val < self.s_min[self.n]:
            self.s_min.append(val)
        else:
            self.s_min.append(self.s_min[self.n])
        self.s.append([val, self.s_min])
        self.n +=1
    def pop(self) -> None:
        if self.n >= 0:
            self.s.pop()
            self.s_min.pop()
            self.n -=1
    def top(self) -> int:
        if self.n >= 0:
            return self.s[self.n][0]
    def getMin(self) -> int:
        return self.s_min[self.n]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
