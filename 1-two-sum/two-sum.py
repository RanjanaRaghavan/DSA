class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map1 = collections.defaultdict(int)

        for i,n in enumerate(nums):
            comp = target - n
            
            if comp in map1:
                return [i,map1[comp]]
            
            map1[n] = i
    
        