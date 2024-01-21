class Solution:

    # Use DP. Iterate thru s, consider all substrings (j:i) of s. 
    #   If (0:j) can be segmented and s[j:i] is a word in wordDict, (0:i) can be segmented
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        # Get largest len of all words in wordDict. Then we will only consider substrings
        #   of s with length <= max_len
        max_len = max(map(len, wordDict))
        for i in range(1, length + 1):
            if dp[i]: continue

            for j in range(i-1, i - max_len -1, -1):
                # (0:i) is segmentable. Set dp[i] to true and break early
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break

        # Value at index 'length' stores if the whole string 's' is segmentable 
        return dp[length]