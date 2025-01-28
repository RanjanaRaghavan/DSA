class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        '''
        1. sort the nums
        2. have two left and right pointers to find complement increase counter
            left = 0
            right = len(nums) -1
        3. return counter after loop ends
        '''
        nums.sort()

        left = 0
        right = len(nums) -1
        count = 0

        while left < right:

            #Case 1 : Good case
            if nums[left] + nums[right] == k:
                count +=1
                left +=1
                right -=1
            
            elif nums[left] + nums[right] < k:
                left +=1
            
            else:
                right -=1
        
        return count

        