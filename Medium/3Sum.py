class Solution:
    
    # Sort input into three groups, positive, negative and zero
    #   If there are at least three zeroes, we can add a tuple of all zeroes
    #   If there is at least one zero, we can add every positive number who's complement is in the negative set to the ans
    #   For every combination of two negatives, if the complement of their sum is in the positive set, we can add these three to the ans4
    #   Vice-versa for the positives
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        zeroes, positives, negatives = 0, [], []
        pSet, nSet = set(), set()
        
        # Sort into groups
        for num in nums:
            if num > 0:
                positives.append(num)
                pSet.add(num)
            elif num < 0:
                negatives.append(num)
                nSet.add(num)
            else:
                zeroes += 1
        
        ans = set()

        # At least three zeroes
        if zeroes >= 3:
            ans.add((0, 0, 0))

        # At least one zero, can add any x in pSet if -x is in nSet
        if zeroes:
            for num in pSet:
                if -1 * num in negatives:
                    ans.add((-1 * num, 0, num))

        lenN = len(negatives)
        lenP = len(positives)

        # For any pair x,y in negatives, if -(x + y) is in positives, can add these 3
        for i in range(lenN):
            for j in range(i+1, lenN):
                target = -1 * (negatives[i] + negatives[j])
                if target in pSet:
                    ans.add(tuple(sorted([negatives[i], negatives[j], target])))
        
        # For any pair x,y in positives, if -(x + y) is in negatives, can add these 3
        for i in range(lenP):
            for j in range(i + 1, lenP):
                target = -1 * (positives[i] + positives[j])
                if target in nSet:
                    ans.add(tuple(sorted([positives[i], positives[j], target])))
        
        return ans

        

        
            
        