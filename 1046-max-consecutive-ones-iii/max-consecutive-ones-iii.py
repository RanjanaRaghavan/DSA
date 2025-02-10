class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        count = 0 
        max_c = 0
        for right in range(len(nums)):

            print(right, count, max_c)

            if nums[right] == 0:
                count +=1
            
            while count > k:
                #keep looping till we can encounter the first 0
                if nums[left] == 0:
                    count -=1
                
                left +=1
            
            #calculate the max
            max_c = max(max_c, right - left +1)
        
        return max_c


        