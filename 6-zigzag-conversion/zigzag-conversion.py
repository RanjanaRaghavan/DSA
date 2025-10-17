class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s

        row = [''] * numRows
        down = False
        cur_row = 0

        for c in s:
            print(c)
            row[cur_row] += c

            #if we hit the top or bottom row we toggle the direction
            if cur_row == 0 or cur_row == numRows -1:
                down = not down
            
            if down:
                cur_row +=1
            else:
                cur_row -=1
        
        return ''.join(row)

