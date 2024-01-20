class Solution:

    # Simple evaluation with a stack. When we see an operator, pop last 2 nums, do the operation, push result
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            match item:
                case '+':
                    stack.append(stack.pop() + stack.pop())

                # Order matters, first thing on stack is the second argument to subtraction
                case '-':
                    second = stack.pop()
                    stack.append(stack.pop() - second)

                case '*':
                    stack.append(stack.pop() * stack.pop())

                # Order matters, first thing on stack is the second argument to division
                case '/':
                    second = stack.pop()
                    stack.append(int(stack.pop() / second))

                # item is not an operator so it must represent a number, push to stack
                case _:
                    stack.append(int(item))

        # Final answer is the only thing left in the stack
        return stack.pop()