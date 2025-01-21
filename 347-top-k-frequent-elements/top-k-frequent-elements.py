class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ctr = Counter(nums)
        min_heap = []

        if(k == len(nums)):
            return nums
        
        return heapq.nlargest(k, ctr.keys(), key=ctr.get)


        