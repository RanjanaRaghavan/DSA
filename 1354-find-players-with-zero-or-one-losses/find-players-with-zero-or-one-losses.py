class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        '''
            Two Sets
            1. Winner : key ->player 
            2. Loser : key ->player 

            One dict:
            1.Loser : key->player val->freq beacause we only care about loser freq 
            
            One list for output
            1.Output = []

            Do:
            1. Loop through matches and keep populating both dicts
            2. process values of both dicts and update output list
        '''

        output = []

        #base case
        if len(matches) < 1:
            return output
        
        #Two Sets
        winner_set = set(match[0] for match in matches)
        

        #1 dict for freq
        loser_dict =  collections.Counter(match[1] for match in matches)
        loser_set = set(loser_dict.keys())

        
        
        for key,value in loser_dict.items():

            if key in winner_set:
                winner_set.remove(key)
            
            if value != 1:
                loser_set.remove(key)
        

        return [sorted(list(winner_set)),sorted(list(loser_set))]

    



    

        