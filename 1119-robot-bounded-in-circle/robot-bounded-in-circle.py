class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        #Base condition
        if len(instructions) <=1:
            return False

        #Start Condition
        row = 0
        col = 0

        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        #If travelling N or S -> col pointer +1 , -1
        #If travelling E or W -> row pointer +1, -1
        #Only G means Go
        idx = 0

        for i in instructions:

            if i == 'R':
                idx = (idx + 1) % 4
            
            elif i == 'L':
                idx = (idx +3) % 4
            
            else:
                row += directions[idx][0]
                col += directions[idx][1]
        
        return (row == 0 and col == 0) or idx != 0






        