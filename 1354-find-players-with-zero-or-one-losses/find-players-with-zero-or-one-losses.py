class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        '''
            Two Dicts
            1. Winner : key ->player , val-> freq
            2. Loser : key ->player , val-> freq
            
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
        
        #Two Dicts
        winner_dict = collections.Counter(match[0] for match in matches)
        loser_dict =  collections.Counter(match[1] for match in matches)

        #print(winner_dict,loser_dict)

        #list of all players that have not lost any matches.
        ''' 
            1.Winner List
                We need to compare both lists and ensure the loser list doesnt 
                have key which is in winner list
        '''
        
        for key in loser_dict.keys():

            if key in winner_dict:
                winner_dict.pop(key)

        '''
            2.Loser List
                a list of all players that have lost exactly one match.
                so value must be 1
        '''
        loser_copy = loser_dict.copy()
        for key,value in loser_copy.items():
            
            if value != 1:
                loser_dict.pop(key)
        

        return [sorted(list(winner_dict.keys())),sorted(list(loser_dict.keys()))]

    



    

        