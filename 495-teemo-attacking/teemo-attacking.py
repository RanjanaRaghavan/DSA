class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        '''
        Approach
        1. Initialize a counter
        2. if next attack is <= time + duration -1 then attack resets.
        3. so reset = newtime - old time + time + duration -1
        4. Calculate total seconds
        5. Return Counter
        '''
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        t = len(timeSeries)
        seconds = 0

        for i in range(t):
            if i+1 < t and timeSeries[i+1] <= timeSeries[i] + duration -1:
                seconds+= timeSeries[i+1] - timeSeries[i]
            else:
                seconds += duration
        
        return seconds

# def test_findPoisonedDuration():

#     sol = Solution()
#     #regular
#     assert sol.findPoisonedDuration([1,4],2) == 4
#     #min
#     assert sol.findPoisonedDuration([1,4],0) == 0
#     #max
#     assert sol.findPoisonedDuration([1,4],10) == 13
#     #no op
#     assert sol.findPoisonedDuration([1],0) == 0
#     #same
#     assert sol.findPoisonedDuration([1,1],1) == 1

# test_findPoisonedDuration()
# print("All tests passed!")
        