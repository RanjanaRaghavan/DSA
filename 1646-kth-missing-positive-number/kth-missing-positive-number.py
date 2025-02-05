class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        for i in range(1,len(arr)+1+k):
            if i not in arr:
                k = k-1
            if k ==0:
                return i
        