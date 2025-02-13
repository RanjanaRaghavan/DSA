class Solution:
    def isPalindrome(self, s: str) -> bool:

        ispal = ''

        for c in s:
            if c.isalnum():
                ispal += c.lower()
        
        return ispal == ispal[::-1]
        