class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(grid,i,j,visited):

            Q = collections.deque([[i,j]])
            visited[i][j] = 1

            while Q:

                r,c = Q.popleft()
                
                
                directions = [(0,1),(0,-1),(1,0),(-1,0)]

                for dr,dc in directions:

                    nr = r +dr
                    nc = c +dc

                    if 0 <= nr < len(grid) and 0<= nc < len(grid[0]) and grid[nr][nc] == "1" and visited[nr][nc] == 0:
                        visited[nr][nc] =1
                        Q.append([nr,nc])


        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        count = 0

        if not grid :
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    bfs(grid,i,j,visited)
                    count +=1
    
        return count



        

        