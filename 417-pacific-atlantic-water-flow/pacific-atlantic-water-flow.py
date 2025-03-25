class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        
        pacific_Q = collections.deque()
        atlantic_Q = collections.deque()

        rows , cols = len(heights), len(heights[0])

        #Populate the Queues with all possible points of overflow
        for i in range(rows):
            pacific_Q.append((i,0))
            atlantic_Q.append((i,cols-1))
        
        for i in range(cols):
            pacific_Q.append((0,i))
            atlantic_Q.append((rows -1,i))
        
        #print(pacific_Q , atlantic_Q)
        
        #Helper Func BFS
        def bfs(Queue):
            reachable = set()
            while Queue:
                r,c = Queue.popleft()
                reachable.add((r,c))
                
                for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:

                    new_r = r+x
                    new_c = c+y

                    # is it out of bounds?
                    if new_r <0 or new_r >= rows or new_c < 0 or new_c >=cols:
                        continue

                    # is it already visited?
                    if (new_r , new_c) in reachable:
                        continue

                    #is it of greater height?
                    if heights[new_r][new_c] < heights[r][c]:
                        continue
                    
                    #Here we can add to Q
                    Queue.append((new_r,new_c))

            return reachable
        
        pacific_reachable = bfs(pacific_Q)
        atlantic_reachable = bfs(atlantic_Q)

        return list(pacific_reachable.intersection(atlantic_reachable))




        

        