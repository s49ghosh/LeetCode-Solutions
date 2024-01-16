class Solution:
    
    # Loop thru ransom note, for every char look for a match in magazine
    #   If exists, replace it with an empty char to 'use' it
    #   If not, return False
    # If we make it thru the whole note, ret True
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                index = magazine.index(char)
                magazine = magazine.replace(char, "", 1)
            else:
                return False
        return True