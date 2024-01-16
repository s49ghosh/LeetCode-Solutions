class Solution:
    
    # Turn both strings into lists, and then sort them
    #   If they result in the same list, they are anagrams
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        listS.sort()
        listT.sort()
        return listS == listT