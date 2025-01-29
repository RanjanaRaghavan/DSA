class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        '''
            1. its freq are equal -> order doesnt matter so u can swap around
            2. all the values are equal in ctr
        '''

        #Base case
        if len(word1) != len(word2):
            return False

        ctr1 = Counter(word1)
        ctr2 = Counter(word2)


        #check for key
        for key in ctr1:
            if key not in ctr2:
                return False

        #check for val
        val1 = sorted(list(ctr1.values()))
        val2 = sorted(list(ctr2.values()))
        
        if val1 != val2:
            return False

        return True
    




        
        