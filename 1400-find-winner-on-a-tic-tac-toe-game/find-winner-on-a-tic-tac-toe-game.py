class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        #Base Case - U need atleast 5 moves for a win 
        if len(moves) < 5:
            return "Pending"

        board = [' '] * 10

        #Add the moves in board
        player_is_x = True
        for move in moves:
            pos = (move[0] * 3) + move[1] + 1
            
            if player_is_x:
                player = 'A'
                player_is_x = False
            else:
                player = 'B'
                player_is_x = True

            board[pos] = player

        #Win Logic

        #Check row
        for row in range(1,8,3):
            if board[row] == board[row+1] == board[row+2] and board[row]!=' ':
                return board[row]

        #check cols  
        for col in range(1,4):
            if board[col] == board[col+3] == board[col+6] and board[col]!= ' ':
                return board[col]

        #check diagnols
        if (board[1] == board[5] == board[9] and board[5]!= ' ') or \
           (board[3] == board[5] == board[7] and board[5]!= ' '):
            return board[5] 

        #if none of them work check for pending condition
        if len(moves) < 9:
            return "Pending"
        
        return "Draw"