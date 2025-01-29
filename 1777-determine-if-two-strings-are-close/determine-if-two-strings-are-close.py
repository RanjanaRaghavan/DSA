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


        return set(ctr1.keys()) == set(ctr2.keys()) and sorted(ctr1.values()) == sorted(ctr2.values())
    




        
        