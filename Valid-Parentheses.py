class Solution:

    # Approach: Map each opening parenthesis to its respective closing parenthesis
    #   Use a stack to maintain open parentheses that have been seen
    #   Everytime a closing parenthesis is encountered, check if the top of the stack matches it
    #   At the end, string is valid if stack is empty
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '[': ']', '{': '}'}
        
        stack = []
        for bracket in s:
            # Opening Parenthesis
            if bracket in hashmap:
                stack.append(bracket)
            
            # Closing Parenthesis
            elif not stack or hashmap[stack.pop()] != bracket:
                return False
        
        return not stack