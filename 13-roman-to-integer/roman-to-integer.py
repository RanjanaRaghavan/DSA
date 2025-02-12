class Solution:
    def romanToInt(self, s: str) -> int:

        map1 = {
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

            cur = map1[s[i]]
            nxt = map1[s[i+1]] if i+1 < len(s) else 0

            if cur < nxt:
                res -= cur
            else:
                res += cur
        
        return res


        