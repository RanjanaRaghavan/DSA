class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #Base Case
        if len(nums) == 0:
            return 0
            
        pref_dict = collections.defaultdict(int)
        pref_dict[0] =1

        pref_sum = 0
        res = 0
        for n in nums:
            pref_sum +=n
            comp = pref_sum - k 
            
            if comp in pref_dict:
                res += pref_dict[comp]
            
            pref_dict[pref_sum] +=1
        
        return res


        