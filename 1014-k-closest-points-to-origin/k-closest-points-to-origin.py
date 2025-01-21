class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        '''
        A maxHeap to store kth closest points to origin
        key -> distance
        value -> point
        '''

        max_heap = []

        for point in points:

            dist = math.sqrt( (point[0] * point[0]) +  (point[1] * point[1])) 
            
            heapq.heappush(max_heap,[-dist,point])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for dist,point in max_heap]
        