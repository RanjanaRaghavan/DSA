class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        left = 0
        right =0

        maxavg = float('-inf')
        total = 0

        while right < len(nums):
            
            if right - left >= k:
                maxavg = max(maxavg, total /k)
                total -= nums[left]
                left += 1


            total += nums[right]
            right +=1
        
        #end of loop check
        maxavg = max(maxavg, total/k)
            
        return maxavg

        