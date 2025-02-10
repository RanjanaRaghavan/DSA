class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        map1 = {}
        left =0
        c = 0

        for right in range(len(s)):

            if s[right] in map1 and map1[s[right]] >= left:
                left = map1[s[right]]+1

            map1[s[right]] = right
            c = max(c, right - left +1)
        
        return c

        