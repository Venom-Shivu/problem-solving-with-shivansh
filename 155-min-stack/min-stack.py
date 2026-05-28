class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        if self.stack:
            curr_min = self.stack[-1][1]

            if val < curr_min:
                curr_min = val
        else:
            curr_min = val

        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]