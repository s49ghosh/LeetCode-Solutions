class Solution:
    
    # Approach: Check if every char matches the char on the other side of the string
    #   We only need to do this until half of the string
    def isPalindrome(self, s: str) -> bool:

        # String could contain uppercase chars, make them lowercase
        s = s.lower()

        # Remove all non-alphanumeric chars
        s = ''.join(filter(str.isalnum, s))
        length = len(s)

        # Perform the check. The respective char for i is at len - i - 1. 
        #   For example, i = 0, its counterpart is len - 0 - 1 = len - 1.
        for i in range(length // 2):
            
            if s[i] != s[length - 1 - i]:
                return False
            
        return True