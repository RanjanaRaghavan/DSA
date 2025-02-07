class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        for p in points:

            dist = math.sqrt(p[0] ** 2 + p[1] **2)
            
            heapq.heappush(res,[-dist,p])

            if len(res) > k:
                heapq.heappop(res)
        
        return [point for dist,point in res]


        