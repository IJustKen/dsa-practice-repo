# SLOW METHOD: keeping ONE stack which stores tuples like (val, min_at_the_time_this_was_pushed)
# this unnecessarily creates 2 values for every single push.
# imagine you pushed 10000 times and min is same, it is redundant info being kept
class MinStack:
    def __init__(self):
        self.stack = list()
        self.curr = float('inf')

    def push(self, value: int) -> None:
        if value < self.curr:
            self.curr = value
        self.stack.append((value, self.curr))
    def pop(self) -> None:
        val, min_hist = self.stack.pop()
        if min_hist == self.curr:
            if len(self.stack) != 0:
                self.curr = self.stack[-1][1]
            else:
                self.curr = float('inf')
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.curr

# FASTER METHOD: keep 2 stacks, one tracks the actual stack and one tracks the minimums
class MinStack:
    def __init__(self):
        self.stack = list()
        self.minstack = list()

    def push(self, value: int) -> None:
        self.stack.append(value)
        # consider equal to case as well, as imagine pushing 0,1,0 will push two minimums which are 0,0
        # so we cannot just keep one of em in the minstack as popping the last 0 will pop the only 0 in the minstack
        # even though the first 0 remains in the actual stack and is the min
        if not self.minstack or self.minstack[-1] >= value:
            self.minstack.append(value)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

