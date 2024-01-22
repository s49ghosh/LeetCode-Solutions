class Solution:

    # A monotonic stack is perfect here. 
    #   Monotonically decreasing, as we want to find the next largest element
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        
        # Loop thru temps
        for i in range(length):
            # While temp @ top of stack is smaller than current temp, pop
            #   To maintain monotonic decreasing property
            #   When we pop, we know the current index is the next larger element from the index at the top of the stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                ans[prev] = i - prev
            
            stack.append(i)
        
        return ans