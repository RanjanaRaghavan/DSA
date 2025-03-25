class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        atlantic_Q = collections.deque()
        pacific_Q = collections.deque()

        rows,cols = len(heights),len(heights[0])

        #Populate Queues

        for i in range(rows):
            atlantic_Q.append((i,cols-1))
            pacific_Q.append((i,0))


        for i in range(0,cols):
            atlantic_Q.append((rows-1,i))
            pacific_Q.append((0,i))

        
        def bfs(Queue):
            
            reachable = set()
            while Queue:

                r,c = Queue.popleft()
                reachable.add((r,c))

                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:

                    nr,nc = r+x , y+c

                    #is the new r,c out of bounds
                    if nr <0 or nr>=rows or nc<0 or nc>=cols:
                        continue
                    #is it already in reachable
                    if (nr,nc) in reachable:
                        continue
                    #is it of greater height
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    
                    Queue.append((nr,nc))
                
            return reachable
        
        atlantic_set = bfs(atlantic_Q)
        pacific_set = bfs(pacific_Q)

        return list(pacific_set.intersection(atlantic_set))


        
        