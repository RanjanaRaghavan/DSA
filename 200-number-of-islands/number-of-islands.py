class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(grid,r,c,count):
            Q = collections.deque([[r,c]])

            while Q:
                #print(Q)
                r,c = Q.popleft()
                grid[r][c] = "0"

                directions = [(-1,0),(1,0),(0,-1),(0,1)]

                for dr,dc in directions:
                    nr = dr +r
                    nc = dc +c

                    if 0 <= nr < len(grid) and 0<=nc <len(grid[0]) and grid[nr][nc] == "1" and [nr,nc] not in Q:
                        Q.append([nr,nc])
        
        if not grid :
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(grid,i,j,count)
                    count +=1
        
        return count
            
        



        