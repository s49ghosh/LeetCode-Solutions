class MinStack:

    # Use two stacks, one to hold the values, one to hold the min at the current time
    def __init__(self):
        self.stack = []
        self.min = []
        
    # Basic push onto the value stack. For the min stack, push the smaller of the old min and val
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(val if not self.min else min(self.min[-1], val))
        
    # Can just pop from both, as the min holds the min corresponding to the val 
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    # Basic top functions
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()