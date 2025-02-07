class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        map1 = collections.defaultdict(int)
        left = 0
        count = 0
        
        for right in range(len(s)):
            
            #Add to Map
            map1[s[right]] +=1

            #check for window and maxFreq
            maxFreq = max(map1.values())
            window = right - left +1

            if window - maxFreq > k:
                map1[s[left]] -=1
                left +=1
        
            #Calculate max count and update
            count = max(count, right - left +1)
        
        return count



            






        