class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        #Base case
        if str1+str2 != str2+str1:
            return ''
        
        a = len(str1)
        b = len(str2)

        if a >b:
            gcf = gcd(a,b)
        else:
            gcf = gcd(b,a)
        return str1[0:gcf]

    def gcd(a,b):
        if b == 0:
            return a
        
        return gcd(b,a % b)


        