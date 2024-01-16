# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    # Binary search approach. If mid is bad and 1st version, return mid
    #   If mid is bad and prev version is not, return mid
    #   if mid is bad, prev is also bad, we need to search from 1..mid - 1
    #   if mid is not bad, we need to search from mid+1..n
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while True:
            mid = (right + left) // 2
            
            if isBadVersion(mid): 
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                
                else:
                    right = mid - 1
            
            else:
                left = mid + 1

        
        