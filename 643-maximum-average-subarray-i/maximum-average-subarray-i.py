class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sumk = sum(nums[:k])
        max_sum = sumk

        for i in range(k,len(nums)):
            
            sumk = sumk - nums[i-k] + nums[i]
            max_sum = max(max_sum,sumk)

        return max_sum/k