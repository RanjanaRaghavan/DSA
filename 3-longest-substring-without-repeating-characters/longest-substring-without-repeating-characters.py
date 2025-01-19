class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        set1 = set()
        maxCount =0
        left =0
        for right in range(len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left+=1
            
            set1.add(s[right])
            maxCount = max(maxCount, right - left +1)
        
        return maxCount
             
