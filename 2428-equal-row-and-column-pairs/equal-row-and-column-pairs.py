class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        '''
        1.Transpose Matrix
            reverse
        2.Compare rows with colums
        '''
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        transpose = [[0] * rows for _ in range(cols)]

        #Transpose
        for i in range(rows):
            for j in range(cols):
                transpose[i][j] = grid[j][i]

        #Counter of transpose
        ctr = Counter(tuple(row) for row in transpose)

        for g in grid:
            if tuple(g) in ctr:
                count += ctr[tuple(g)] 
        
        return count


        