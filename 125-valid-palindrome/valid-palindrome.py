class Solution:
    def isPalindrome(self, s: str) -> bool:

        reverse = ''

        for c in s:
            if c.isalnum():
                reverse += c.lower()

        print(reverse)
        return reverse == reverse[::-1]
        