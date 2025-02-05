class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        if x % 10 ==0 and x != 0:
            return False
        
        revNum = 0
        xCopy = x

        while x > 0:
            revNum = (revNum*10) + (x % 10)
            x = x // 10
        
        return revNum == xCopy
        