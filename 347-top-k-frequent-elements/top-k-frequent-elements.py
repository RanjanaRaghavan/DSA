class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == k:
            return nums
        
        ctr = Counter(nums)
        min_heap = []

        for num,freq in ctr.items():

            heapq.heappush(min_heap,[freq,num])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [k for v,k in min_heap]
