class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]
        right = [1]

        ans = [0] * len(nums)

        #calculate left sum
        for i in range(0,len(nums)-1):
            left.append(left[-1] * nums[i])

        #calculate right sum
        for i in range(len(nums)-1, 0, -1):
            right.append(right[-1] * nums[i])

        right = right[::-1]
        #ans = prefix * suffix
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]

        return ans

        