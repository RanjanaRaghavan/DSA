class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        minheap = []

        for num in arr:
            val = abs(num - x)

            heapq.heappush(minheap,[-val,-num])

            if len(minheap) > k:
                heapq.heappop(minheap)
        
        result = []

        for val,num in minheap:
            result.append(-num)
        
        result.sort()

        return result
        