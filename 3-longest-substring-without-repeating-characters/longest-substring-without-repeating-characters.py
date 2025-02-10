class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
            1. Have a set to store chars (we dont want repeating chars)
            2. two vars left and right to caluclate length
            3. while u see a repeated char move left pointer
            4. return max length
        '''

        set1 = set()
        max_count = 0
        left = 0

        for right in range(len(s)):

            while s[right] in set1:
                set1.remove(s[left])
                left+=1
                
            set1.add(s[right])
            max_count = max(max_count, right - left +1)
        
        return max_count

        