class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        '''
        sort the array 
        get the product of first 3 elements or first two small and last element
        if sorted array is [a,b,c,...x,y,z]
        basically max(abz,xyz)
        '''

        #Base Cases

        if len(nums) < 3:
            return -1

        nums.sort()
        
        l = len(nums)
        product_pos = nums[l-1] * nums[l-2] * nums[l-3]
        product_neg = nums[0] * nums[1] * nums[l-1]
    
        
        return max(product_pos,product_neg)
        