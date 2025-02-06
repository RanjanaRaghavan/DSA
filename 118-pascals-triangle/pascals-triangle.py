class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return [[]]

        pascal = [[1]]

        for i in range(1,numRows):

            cur_level = [1]
            prev_level = pascal[i-1]

            for j in range(1,i):

                cur_level.append(prev_level[j] + prev_level[j-1])

            cur_level.append(1)
            pascal.append(cur_level)
        
        return pascal
        