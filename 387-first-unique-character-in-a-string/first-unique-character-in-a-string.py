class Solution:
    def firstUniqChar(self, s: str) -> int:

        '''
        Map
        '''
        char_dict = collections.Counter(s)

        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i

        return -1
        