class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        '''
        prefix = flower
        5
        0


        '''
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for word in strs[1:]:

            #Cut the prefix short if next word is shorter
            if len(word) < len(prefix):
                prefix = prefix[:len(word)]

            for i in range(len(word)):
                if i >= len(prefix) or word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        
        return prefix