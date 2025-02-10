class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
            1. Have a map to store chars (we dont want repeating chars)
            2. two vars left and right to caluclate length
            3. while u see a repeated char and the value of its last index is greater 
            than left move left pointer to that place + 1 cuz we know thats wer our streak breaks
            4. return max length
        '''

        map1 = {}
        max_count = 0
        left = 0

        for right in range(len(s)):

            if s[right] in map1 and map1[s[right]] >= left:
                left = map1[s[right]] +1
            
                
            map1[s[right]] = right
            max_count = max(max_count, right - left +1)
        
        return max_count

        