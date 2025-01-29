class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        totalsum = sum(nums)
        p_sum = 0
        for i,num in enumerate(nums):

            if totalsum - num - p_sum == p_sum:
                return i

            p_sum += num

        return -1

            

        