class Solution:

    # Store counts in hashmap, if count exceeds floor(length // 2), we're done
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        length = len(nums)
        
        for item in nums:
            hashmap[item] += 1
            
            if hashmap[item] > length // 2:
                return item