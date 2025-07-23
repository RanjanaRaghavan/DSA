class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
        Approach
        1. Sort list and add first element to new list
        2. if newlist[-1][1] < intervals[i][0]
        3. Then min (newlist[-1][0] , intervals[i][0])
            a. max (newlist[-1][1] < intervals[i][1])
            b. else add the interval in
        4. return new list
        '''
        '''
        Time Complexity : O(n) -> n = len(intervals)
        Space Complexity : O(n) -> n = len(intervals) (worst case scenario of no overlap)
        '''
        intervals.sort()
        merged_intervals = [intervals[0]]

        for i in range(1,len(intervals)):
            if merged_intervals[-1][1] >= intervals[i][0]:
                merged_intervals[-1][0] = min(merged_intervals[-1][0] , intervals[i][0])
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            else:
                merged_intervals.append(intervals[i])
                
        
        return merged_intervals

def test_merge():

    sol = Solution()

    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    

        



        