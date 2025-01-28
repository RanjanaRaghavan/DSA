class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s)==0 or (len(s) ==0 and len(t)==0):
            return True

        if len(t) == 0:
            return False

        p1 = 0
        p2 =0

        count = 0
        for p2 in range(len(t)):
            #move pointer p1 if the letters are equal
            if t[p2] == s[p1]:
                count +=1
                p1 +=1
            
            if count == len(s):
                return True

        return False  

        
        