class Trie:
    
    # Can efficiently implement as a dict of dicts
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        # Iterate thru a character at a time
        for char in word:
            # Char not in the dictionary at the current node, add it
            if char not in curr:
                curr[char] = {}

            # Go to the dictionary at index 'char'
            curr = curr[char]
        
        # After we finished the loop, we're at the dictionary of the last char of the word.
        #   Add an entry for the null terminator to signify a word ends here
        curr['\0'] = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        # Iterate thru a character at a time
        for char in word:
            # Char not in the dictionary at the current node, so word is not in our Trie
            if char not in curr:
                return False
            
            # Go to the dictionary at index 'char'
            curr = curr[char]

        # After we finished the loop, we're at the dictionary of the last char of the word.
        #   If the null terminator is in this dict, a word ends here, so the word we were searching for is in our Trie
        return '\0' in curr
        

    def startsWith(self, prefix: str) -> bool:
        # Same logic to traverse Trie
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            
            curr = curr[char]
        
        # If we got this far we can return True, even if there is no null terminator, since we are just looking for a prefix.
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)