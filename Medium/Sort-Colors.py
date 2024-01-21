class Solution:

    # Use the Dutch Flag Algorithm. 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            # If the element at white is 0, it should be before red.
            #   So swap red and white, increment both
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # Element at white is 1, which is what we want. Increment white
            elif nums[white] == 1:
                white += 1
            # Element at white is 2, it should be after blue.
            #   So swap white and blue, decrement blue
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        
        