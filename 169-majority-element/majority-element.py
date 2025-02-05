class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ctr = Counter(nums)

        maxval = -1
        ans = 0
        
        for k,v in ctr.items():
            if v > maxval:
                maxval = v
                ans = k
        
        return ans
            

        