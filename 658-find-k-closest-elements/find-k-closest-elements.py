class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        min_heap = []

        for num in arr:

            val = abs(num - x)

            #check if val exists in heapq
            # if -val in min_heap:
            heapq.heappush(min_heap,[-val,-num])

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return sorted([-num for val,num in min_heap ])

            
        