class MyQueue:

    # Use 2 stacks, on peek move everything from real stack to other stack, if other stack is empty
    def __init__(self):
        self.stackNormal = []
        self.stackFake = []
        

    def push(self, x: int) -> None:
        self.stackNormal.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.stackFake.pop()

    def peek(self) -> int:
        if not self.stackFake:
            for i in range(len(self.stackNormal)):
                self.stackFake.append(self.stackNormal.pop())
        return self.stackFake[-1]
        

    def empty(self) -> bool:
        return not self.stackNormal and not self.stackFake
        