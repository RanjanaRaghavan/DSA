class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        1. Calculate left product
        2. Calculate right product
        3. Multiply both
        '''
        left = [1]
        right = [1]
        ans = [0] * len(left)

        #left Prefix Profuct

        for i in range(0,len(nums)-1):
            left.append(left[-1] * nums[i])

        #Right Prefix Product
        for i in range(len(nums)-1,0,-1):
            right.append(right[-1] * nums[i])

        right = right[::-1]
        print(len(right),len(left))
        #Ans
        for i in range(len(left)):
            right[i] = left[i] * right[i]
        
        return right
        