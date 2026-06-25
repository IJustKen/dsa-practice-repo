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
