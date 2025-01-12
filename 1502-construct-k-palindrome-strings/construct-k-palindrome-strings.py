class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        #Edge Cases
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        #Create an Array of 26 length filled with 0
        lettersArray = [0] * 26

        #loop through the string s and count the freq of each char
        for i in range(len(s)):
            pos = ord(s[i]) - 97
            lettersArray[pos] +=1
        
        #Calculate the number of chars with odd freq
        oddCount =0
        for i in range(26):
            if lettersArray[i] %2 !=0:
                oddCount +=1

        #Logic
        if oddCount >k:
            return False
        else:
            return True

        