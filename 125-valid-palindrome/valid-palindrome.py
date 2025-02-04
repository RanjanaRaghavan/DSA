class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.strip()
        pal = ''

        for c in s:

            if c.isalnum():
                pal += c.lower()
        
        return pal == pal[::-1]
        