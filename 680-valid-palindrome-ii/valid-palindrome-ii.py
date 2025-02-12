class Solution:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) -1

        while i < j:

            if s[i] != s[j]:
                one = s[i+1 : j+1]
                two = s[i:j] #j is not included so no need -1 
                print(one, two)
                return one == one[::-1] or two == two[::-1]
               
            i +=1
            j -=1
        return True

        