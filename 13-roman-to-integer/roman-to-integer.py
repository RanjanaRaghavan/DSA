class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        res = 0

        for i in range(len(s)):

            cur = roman[s[i]]
            nxt = roman[s[i+1]] if i+1 <len(s) else 0

            if cur < nxt:
                res -= cur  # Since cur will be added again in the next iteration
            else:
                res += cur
        
        return res





        