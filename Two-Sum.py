class Solution:

    # Use hashmap to map differences to indices. If we find target - nums[i] in hashmap,
    #   we have a pair that sums to our target.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashMap:
                return [i, hashMap[diff]]
            
            hashMap[num] = i