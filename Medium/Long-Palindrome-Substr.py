class Solution:

    # Try each character as a middle character and build a palindrome by expanding on each side
    #   Then try two characters as middle if they are the same
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        ret = s[0]
        longest = 1

        # Try each char as middle
        for i in range(0, length - 1):
            left, right, curLen = i - 1, i + 1, 1
            # While we are inbounds and the characters on either side are the same, expand our palindrome
            while left >= 0 and right < length and s[left] == s[right]:
                curLen += 2
                left -= 1
                right += 1

            # Update return string if we found a longer one
            if curLen > longest:
                longest = curLen
                ret = s[left+1:right]
        
        # Try two chars as middle if they are the same
        for i in range(0, length - 1):
            if s[i] == s[i + 1]:
                left, right, curLen = i - 1, i + 2, 2
                # While we are inbounds and the characters on either side are the same, expand our palindrome
                while left >= 0 and right < length and s[left] == s[right]:
                    curLen += 2
                    left -= 1
                    right += 1
                
                # Update return string if we found a longer one
                if curLen > longest:
                    longest = curLen
                    ret = s[left+1:right]
        
        return ret
            
        