class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #logic
        #Transpose and reverse rows

        cols = len(matrix[0])
        rows = len(matrix)

        for i in range(rows):
            for j in range(i+1,cols):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]

        for row in range(rows):
            matrix[row].reverse()



        