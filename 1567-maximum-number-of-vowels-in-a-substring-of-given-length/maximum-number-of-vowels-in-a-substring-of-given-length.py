class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        '''
            1. Have s string vowels
            2. check for every letter if letter in vowels
            3. after k items chck for maxcount
        '''
        count = 0
        maxcount = 0
        vowels = 'aeiou'
        left = 0 

        for right in range(len(s)):

            if right - left >= k:
                maxcount = max(maxcount,count)
                if s[left] in vowels:
                    count -=1
                left +=1

            if s[right] in vowels:
                count+=1
        
        return max(maxcount,count)


        