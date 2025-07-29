class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        '''
        1. Lets have rCount and dCount
        2. Increment opp counter of element added to Queue
        3. If counter exixts skip adding element to Queue
        4. Result can be announced if len(Q) =1 or rcount || dcount == len(Q) and the other one is 0
        '''

        rcount = 0
        dcount = 0

        Q = collections.deque([])
        for s in senate:
            Q.append(s)

        while len(Q) > 1:
            
            if rcount == 0 and dcount == len(Q):
                return 'Radiant'
            elif dcount == 0 and rcount == len(Q):
                return 'Dire'

            node = Q.popleft()

            if node == 'R':
                if rcount == 0:
                    Q.append('R')
                    dcount +=1
                else:
                    rcount -=1
            else:
                if dcount == 0:
                    Q.append('D')
                    rcount +=1
                else:
                    dcount -=1
            
        
        return 'Dire' if Q.pop() == 'D' else 'Radiant'

# def test_predictPartyVictory():

#     sol = Solution()

#     assert sol.predictPartyVictory("RD") == 'Radiant'
#     assert sol.predictPartyVictory("RDD") == 'Dire'
#     assert sol.predictPartyVictory("RRDDD") == 'Radiant'
#     assert sol.predictPartyVictory("DR") == 'Dire'
#     assert sol.predictPartyVictory("DRRDRDRDRDDRDRDR") == 'Radiant'

# test_predictPartyVictory()
# print("All tests passed!")


            

        