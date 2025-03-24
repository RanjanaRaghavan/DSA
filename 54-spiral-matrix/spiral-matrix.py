class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        '''
        Moves:
        1. left -> right --> we get up row
        2. top -> bottom --> we get right column
        3. right -> left --> we get bottom row
        4. bottom -> top --> we get left column

        '''
        rows , cols = len(matrix), len(matrix[0])
        result = []
        up,down = 0,rows -1
        left,right = 0,cols -1

        while(len(result) < rows * cols):

            #up
            for i in range(left,right+1):
                result.append(matrix[up][i])
            up +=1

            #right
            for i in range(up, down+1):
                result.append(matrix[i][right])
            right -=1

            #down
            if up <= down:
                for i in range(right,left-1,-1):
                    result.append(matrix[down][i])
                down -=1

            #left
            if left <= right:
                for i in range(down,up-1,-1):
                    result.append(matrix[i][left])
                left +=1
        

        return result

        
        