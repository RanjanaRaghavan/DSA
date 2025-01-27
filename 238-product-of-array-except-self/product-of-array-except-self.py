class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #base values
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)

        ans = [1] * len(nums)

        for i in range(1,len(prefix_arr)):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suffix_arr[i] = suffix_arr[i+1] * nums[i+1]
        
        print(prefix_arr,suffix_arr)
        for i in range(len(nums)):
            ans[i] = prefix_arr[i] * suffix_arr[i]
        
        return ans