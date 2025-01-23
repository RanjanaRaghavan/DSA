class Solution:
    def isPalindrome(self, x: int) -> bool:

        #base cases
        #if x is negative 
        #if x ends with 0 then only 0 can be the number 

        if x<0 or (x %10 == 0 and x != 0):
            return False
        x_copy = x
        reversed = 0
        while x:
            temp = x % 10
            reversed = (reversed *10) + temp
            x = x//10
        
        if reversed == x_copy:
            return True
        else:
            return False


        