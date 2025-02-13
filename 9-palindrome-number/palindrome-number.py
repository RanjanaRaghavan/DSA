class Solution:
    def isPalindrome(self, x: int) -> bool:

        #Base Case
        if x<0 or (x%10 ==0 and x!=0):
            return False
            
        rev = 0

        while x > rev:

            rev = (rev *10) + (x%10)
            x = x//10
        

        return rev == x or x == rev//10
        