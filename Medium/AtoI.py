class Solution:

    # Pretty intuitive solution, lots of edge cases though.
    def myAtoi(self, s: str) -> int:
        # Strip all whitespace
        s = s.strip()
        sign = False
        # If s is the empty string, return 0
        if not s: return 0
        # If the first char is a negative sign, set sign to True to indicate this is negative
        if s[0] == '-':
            sign = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        length = len(s)
        i = 0
        curNum = 0
        # Loop thru s
        while i < length and s[i].isdigit():
            # Little trick to go from string to int
            curNum = curNum * 10 + int(s[i])
            i += 1
        
        # If num was negative multiply by -1
        if sign: curNum *= -1
        # Bound between INT_MIN and INT_MAX
        if curNum > 2147483647: curNum = 2147483647
        elif curNum < -2147483648: curNum = -2147483648
        
        return curNum