class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        '''
        1. loop till min length of both
        2. check which one reached its end
        3. append the other one to ans 
        '''

        output = ''
        l1 = len(word1)
        l2 = len(word2)

        for i in range(0,min(l1,l2)):

            output += word1[i] + word2[i]
        
        if l1 > l2:
            output = output + word1[l2:]
        else:
            output = output + word2[l1:]
        
        return output