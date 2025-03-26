class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        Q = collections.deque()
        fresh =0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    Q.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        days = 0
        while Q:

            curlevel = len(Q)
            infected = False
            
            for _ in range(curlevel):

                r,c = Q.popleft()

                for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:

                    nr = r+x
                    nc = c+y

                    if nr<0 or nr >= len(grid) or nc <0 or nc>= len(grid[0]):
                        continue
                    
                    if grid[nr][nc] !=1:
                        continue
                    
                    grid[nr][nc] = 2
                    Q.append((nr,nc))
                    infected = True
                    fresh -=1
            
            if infected:
                days +=1
        
        return -1 if fresh !=0 else days
                    

