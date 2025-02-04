class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(left,right):

            while left < right:

                if s[left] != s[right]:
                    return False
                
                else:
                    left +=1
                    right -=1
            
            return True
        
        left =0
        right = len(s)-1

        while left < right:

            if s[left] == s[right]:
                left +=1
                right -=1

            else:
                return isPalindrome(left+1,right) or isPalindrome(left,right-1)
        
        return True