class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        unique_set = set(nums1)
        result = set()

        for num in nums2:

            if num in unique_set:
                result.add(num)
        
        return list(result)
        