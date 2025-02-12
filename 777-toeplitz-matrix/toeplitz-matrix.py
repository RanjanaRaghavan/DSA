class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        map1 = {}

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r-c not in map1:
                    map1[r-c] = matrix[r][c]
                elif map1[r-c] != matrix[r][c]:
                    return False
        
        return True