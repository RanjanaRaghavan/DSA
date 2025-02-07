class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left = 0
        count =0

        arr = [0] * 26

        for right in range(len(s)):
            
            
            val = ord(s[right])
            arr[val - 65] +=1

            #calculat the max Freq
            maxFreq = max(arr)
            window = right - left +1

            if window - maxFreq > k:
                arr[ord(s[left]) - 65] -=1
                left +=1

            count = max(right - left +1, count)


        return count

        