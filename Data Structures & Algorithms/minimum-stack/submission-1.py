class MinStack:

    def __init__(self):
        self.stack = []
        self.minnum = float('inf')
        self.minnum_track = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minnum:
            self.minnum = val
            self.minnum_track.append(val)
    def pop(self) -> None:
        num = self.stack[-1]
        if num == self.minnum:
            self.minnum_track.pop()
            if self.minnum_track:
                self.minnum = self.minnum_track[-1]
            else:
                self.minnum = float('inf')
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minnum
        
