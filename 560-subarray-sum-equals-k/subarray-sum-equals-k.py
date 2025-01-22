class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        '''
            Prefix Sum

            1. Have a dict to store prefix_sum
            2. pre set dict[0] as 1 
            3. Have a result no_of_subarrays counter
            4. loop through nums 
                * if we see the comp in dict
                    Add to result the ctr[comp]
                * keep setting the prefix sums and freq in dict
        '''

        #Base Case
        if len(nums) == 0:
            return 0
        
        # if len(nums) ==1 and nums[0] == k:
        #     return 1
        

        pref_dict = collections.defaultdict(int)
        pref_dict[0] = 1

        result = 0
        pref_sum = 0

        for num in nums:

            pref_sum += num
            comp = pref_sum - k

            if comp in pref_dict:
                result += pref_dict[comp]

            pref_dict[pref_sum] +=1
        
        return result