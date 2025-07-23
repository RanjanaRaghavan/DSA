class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n

        pref_prod = [1] * n
        suff_prod = [1] * n

        for i in range(1,n):
            pref_prod[i] = pref_prod[i-1] * nums[i-1]
        print("pref" , pref_prod)
        
        for i in range(n-2,-1,-1):
            suff_prod[i] = suff_prod[i+1] * nums[i+1]
        print("suff" , suff_prod)

        for i in range(n):
            answer[i] = pref_prod[i] * suff_prod[i]

        
        return answer

# def test_productExceptSelf():

#     sol = Solution()

#     assert sol.productExceptSelf([1,2,3,4]) == [24,12,8,6]
#     #min
#     assert sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
#     #max
#     assert sol.productExceptSelf([1,2,3,4]) == [24,12,8,6]
#     #same
#     assert sol.productExceptSelf([1,1,1,1]) == [1,1,1,1]
#     #no op
#     assert sol.productExceptSelf([0,0]) == [0,0]

# test_productExceptSelf()
# print("All tests passed")



        