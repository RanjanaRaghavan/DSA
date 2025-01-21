class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        min_heap = []

        for num in arr:

            val = abs(num - x)

            #check if val exists in heapq
            heapq.heappush(min_heap,[-val,-num])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result =  [-num for val,num in min_heap ]
        result.sort()
        return result

            
        