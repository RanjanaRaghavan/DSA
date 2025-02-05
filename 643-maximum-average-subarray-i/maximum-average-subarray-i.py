class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum1 = sum(nums[:k])
        avg = sum1/k

        for i in range(k,len(nums)):
            sum1 = sum1 - nums[i-k] + nums[i]
            avg = max(avg, sum1/k)
        
        return avg
            

        