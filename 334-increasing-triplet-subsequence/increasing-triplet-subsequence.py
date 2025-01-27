class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first_num = max(nums)
        second_num = max(nums)

        for i in range(0,len(nums)):

            if nums[i] > second_num:
                #print(first_num,second_num,nums[i])
                return True
            
            elif nums[i] > first_num:
                second_num = nums[i]
            elif nums[i] < first_num:
                first_num = nums[i]
        
        return False

        