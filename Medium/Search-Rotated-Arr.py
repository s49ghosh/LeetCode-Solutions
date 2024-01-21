class Solution:

    # Do binary search knowing that either (left:mid) or (mid:right) is sorted properly 
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right, mid = 0, length - 1, -1
        
        # Binary search
        while left <= right:
            mid = (left + right) // 2
            # Found it!
            if nums[mid] == target:
                return mid

            # mid > right means the left half is properly sorted. Use it to perform the check 
            #   So if the target is between left and mid, go left, else go right
            if nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1

            # Otherwise, the right half is properly sorted. Use it to perform the check
            #   So if the target is between mid and right, go right, else go left
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
    
        return -1