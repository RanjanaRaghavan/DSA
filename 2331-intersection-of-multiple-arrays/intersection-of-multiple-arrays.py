class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        combined_arr = []
        result = []

        for num in nums:
            combined_arr += num

        ctr = Counter(combined_arr)

        for num,freq in ctr.items():
            if freq == len(nums):
                result.append(num)
        
        result.sort()
        return result