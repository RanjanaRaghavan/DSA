class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        '''

        sort the array in desc order
        get the product of first 3 elements

        '''

        #Base Cases

        if len(nums) < 3:
            return -1

        nums.sort()
        l = len(nums)
        big_nums = nums[l-3:l]
        small_nums = nums[0:2] + [nums[-1]]

        product_pos = 1
        product_neg = 1
        for i in range(0,3):
            product_pos *= big_nums[i]
            product_neg *= small_nums[i]
        
        return product_pos if product_pos > product_neg else product_neg
        