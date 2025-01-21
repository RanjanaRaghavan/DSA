class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #dict for nums1
        ctr = Counter(nums1)

        result = []

        for num in nums2:

            if num in ctr:
                result.append(num)
                ctr[num] -=1
                if ctr[num] == 0:
                    del ctr[num]
        
        return result
        