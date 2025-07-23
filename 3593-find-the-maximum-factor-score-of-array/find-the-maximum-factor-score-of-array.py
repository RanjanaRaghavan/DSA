class Solution:
    def maxScore(self, nums: List[int]) -> int:
        '''
        Approach 
        1. LCM formula -> x*y // gcd(x,y)
        3. Calculate maxfactor for og array
        4. prefix + suffix sum every lcm and gcd to find out which can be ignored to get max factor
        5. Compare and return max num
        '''
        '''
        Time Complexity : O(n)
        Space Complexity : O(n)
        '''
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0] * nums[0]

        def lcm(a,b):
            return a *b //gcd(a,b)
        
        def lcmoflists(nums):
            cur_lcm = nums[0]
            for num in nums[1:]:
                cur_lcm = lcm(cur_lcm, num)
            return cur_lcm

        def gcdoflists(nums):
            cur_gcd = nums[0]
            for num in nums[1:]:
                cur_gcd = gcd(cur_gcd, num)
            return cur_gcd

        factors = []
        maxfactor = gcdoflists(nums) * lcmoflists(nums)

        for i in range(len(nums)):
            new_list = nums[:i] + nums[i+1:]
            new_factor = gcdoflists(new_list) * lcmoflists(new_list)
            maxfactor = max(maxfactor,new_factor)
            print(i,maxfactor)

        
        return maxfactor

# def test_maxScore():

#     sol = Solution()
#     #regular
#     assert sol.maxScore([1,2,3,4,5]) == 60
#     #Min
#     assert sol.maxScore([3]) == 9
#     #Modified
#     assert sol.maxScore([2,4,8,16]) == 64
#     #same
#     assert sol.maxScore([3,3]) == 9
#     #min
#     assert sol.maxScore([]) == 0


# test_maxScore()
# print("All tests passed!")

        
        