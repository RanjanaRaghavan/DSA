class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = collections.defaultdict(int)

        for i,n in enumerate(nums):
            comp = target - n

            if comp in dictionary:
                return [i,dictionary[comp]]
            
            else:
                dictionary[n] = i
        
        