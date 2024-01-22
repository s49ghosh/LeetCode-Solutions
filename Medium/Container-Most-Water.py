class Solution:

    # Use greedy and two pointer. Start a pointer on each end of the container
    #   Greedily move the one that points to a shorter line
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maximum = 0
        while left < right:
            maximum = max(maximum, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            
            else:
                right -= 1
            
        return maximum

        