class Solution:

    # Use a counter to get a count of all frequencies in p.
    #   Iterate through s, decrementing counter if we see a char in s that is in p
    #   If everything in counter is 0, we have an anagram in s, add the starting index
    #   Increment counter as a char leaves our window of consideration
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        lenP = len(p)
        lenS = len(s)
        result = []

        # Iterate through s
        for i in range(lenS):
            # s[i] is in p, decrement the freq in counter
            if s[i] in counter:
                counter[s[i]] -= 1
            
            # Start of the current anagram
            curr = i - lenP + 1

            # If we have considered at least lenP chars
            if curr >= 0:
                # If counter is all 0, anagram found
                if not any(counter.values()):
                    result.append(curr)

                # If start of current anagram is in counter, increment
                #   As next iteration, that char will be out of our window, so we cannot use it in our anagram
                if s[curr] in counter:
                    counter[s[curr]] += 1
                    
        return result
            
            
