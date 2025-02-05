class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        '''
            1. keep thge first word as prefix
            2. Then loop thru every word
                1. compare every character and update prefix
            3. return Prefix
        '''

        prefix = strs[0]

        for s in strs:

            while not s.startswith(prefix):
                prefix =prefix[:-1] 
            
        return prefix








        