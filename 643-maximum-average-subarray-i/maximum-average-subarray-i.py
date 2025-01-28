class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total = sum(nums[:k])
        maxavg = total/k

        for i in range(k,len(nums)):
            total = total - nums[i-k] + nums[i]
            maxavg = max(maxavg, total/k)
        
        return maxavg
        