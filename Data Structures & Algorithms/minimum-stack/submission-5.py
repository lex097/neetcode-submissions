class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.Min = float ('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.Min))
        self.Min = min(val, self.Min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.Min = self.minStack[-1]
        else:
            self.Min = float ('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
