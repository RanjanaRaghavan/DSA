class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l1 = m-1
        l2 = n-1

        for i in range(m+n -1,-1,-1):

            if l2 < 0:
                break

            if l1>=0 and nums1[l1] >= nums2[l2]:
                nums1[i] = nums1[l1]
                l1 -=1
            else:
                nums1[i] = nums2[l2]
                l2 -=1
        
        