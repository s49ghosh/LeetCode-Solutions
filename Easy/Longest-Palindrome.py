class Solution:
    
    # Use counter to count all occurences of chars in s. 
    #   Add length possible from each
    #   If there is any chars with an odd number of occurences, add 1 to maxLen
    def longestPalindrome(self, s: str) -> int:
        maxLen = 0
        freq = Counter(s)
        
        for _,val in freq.items():
            maxLen += (val // 2) * 2
        
        freq = {key: val for key, val in freq.items() if val % 2}
        
        if freq:
            maxLen += 1
        
        return maxLen
        
                