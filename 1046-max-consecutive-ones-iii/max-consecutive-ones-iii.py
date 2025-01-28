class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        '''
         1. if number is 1 we increase counter
         2. if number is 0 we increase flipcounter and counter
         3. while flipcounter is > k
            1. we check if left was 0 if 0 flipcounter -1
            2. regardless counter -1
            3. left +1
        '''

        left = 0
        flipcount = 0
        maxcount = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                flipcount +=1
            
            if flipcount > k:
                maxcount = max(maxcount,right - left)

                while nums[left] != 0:
                    left +=1
                
                #at this point we reached a 0
                flipcount -=1
                left +=1

        
        return max(maxcount, right - left +1)
            
            
        