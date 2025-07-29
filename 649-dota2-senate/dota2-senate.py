class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        '''
        1. Lets have two Queues radiant and dire
        2. Have a i var to determine position
        3. eliminate the senators by compaing pos and put them back in Q
        4. Result can be determined when 1 queue goes empty
        '''
        '''
        Time complexity: O(n)
        Space complexity: O(n) n-> len(senate)
        '''

        n = len(senate)

        radiant = collections.deque([])
        dire = collections.deque([])

        for i,s in enumerate(senate):
                
                if s == 'D':
                    dire.append(i)
                else:
                    radiant.append(i)

        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)             
            
        return 'Dire' if dire  else 'Radiant'

# def test_predictPartyVictory():

#     sol = Solution()

#     assert sol.predictPartyVictory("RD") == 'Radiant'
#     assert sol.predictPartyVictory("RDD") == 'Dire'
#     assert sol.predictPartyVictory("RRDDD") == 'Radiant'
#     assert sol.predictPartyVictory("DR") == 'Dire'
#     assert sol.predictPartyVictory("DRRDRDRDRDDRDRDR") == 'Radiant'

# test_predictPartyVictory()
# print("All tests passed!")


            

        