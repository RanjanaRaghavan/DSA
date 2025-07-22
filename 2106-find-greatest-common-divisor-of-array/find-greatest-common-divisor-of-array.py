class Solution:
    def findGCD(self, nums: List[int]) -> int:

        '''
        1. Find smallest and largest num
        2. % from 2 to small and find gcd
        3. return gcd
        '''
        '''
        Time Complexity : O(s) -> s = small num
        Space Complexity : O(1)
        '''

        small = min(nums)
        large = max(nums)
        gcd = 1

        for i in range(2,small+1):
            if (small % i == 0) and (large % i == 0):
                gcd = i
                
            print(i,gcd)
        
        return gcd

# def test_findGCD():

#     sol = Solution()
#     #min
#     assert sol.findGCD([7,5,6,8,3]) == 1
#     #same
#     assert sol.findGCD([3,3,3,3]) == 3
#     #no op
#     assert sol.findGCD([1,1,1,1]) == 1
#     #regular
#     assert sol.findGCD([2,5,6,9,10]) == 2

# test_findGCD()
# print("All tests passed!")
        