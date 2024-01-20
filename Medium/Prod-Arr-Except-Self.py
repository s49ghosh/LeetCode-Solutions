class Solution:
    
    # Use a prefix and suffix array to compute the desired result
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = 1
        suffProduct = 1
        length = len(nums)
        output = [0] * length
        
        # Make a pass forward thru the array. At each i, store the product of everything before i in the array
        #   In other words, the product of nums[0:i]
        for i in range(length):
            output[i] = preProduct
            preProduct *= nums[i]
        
        # Make a pass backward thru the array, now multiplying output[i] by the product of everything after i in the array
        for i in range(length - 1, -1, -1):
            output[i] *= suffProduct
            suffProduct *= nums[i]

        # Now, each index i contains the product of everything before i * the product of everything after i
        #   So, we have the product of the array, except self, as desired
        return output