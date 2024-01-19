class Solution:

    # One liner in Python LOL
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        