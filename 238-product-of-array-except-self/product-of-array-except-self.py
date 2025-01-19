class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        3 lists
        one for left and right each
        one for ans
        '''
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)
        ans = [1] * len(nums)


        #for loop to iterate through every element of array left to right
        for i in range(1,len(nums)):

            #left array will have everything i-1
            left_arr[i] = left_arr[i-1] * nums[i-1]

        # for loop to iterate from right to left also left * right
        for i in range(len(nums)-1 ,-1,-1):
            if i == len(nums)-1:
                ans[i] = left_arr[i]
            else:
                #right will have everything i+1
                right_arr[i] = right_arr[i+1] * nums[i+1]

                ans[i] = right_arr[i+1] * nums[i+1] * left_arr[i]

            
        return ans
        