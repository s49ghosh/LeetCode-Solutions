class Solution:

    # Sliding Window technique, keep increasing right as long as no repeats.
    #   When we see a repeat, set left to last occurence of the char + 1
    #   Then l to r has no repeats, we can continue
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        longest = 0
        left = 0

        # Iterate right from 0 to len - 1
        for r in range(len(s)):
            # Char in seen hashmap and we last saw it in an index > left, so s[r] is a repeat
            if s[r] in lastSeen and lastSeen[s[r]] >= left:
                left = lastSeen[s[r]] + 1
            
            # Update last seen
            lastSeen[s[r]] = r
            longest = max(longest, r - left + 1)
        
        return longest
