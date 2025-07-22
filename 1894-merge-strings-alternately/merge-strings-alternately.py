class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        '''
        iterations
        when l2 or l1 ends then append rest of string
        '''
        l1 = len(word1)
        l2 = len(word2)
        ans = []
        for i in range(0,min(l1,l2)):
                ans.append(word1[i]) 
                ans.append(word2[i])
        
        if l1 > l2:
            ans.append(word1[l2:])
        else:
            ans.append(word2[l1:])
        return ''.join(ans)

        