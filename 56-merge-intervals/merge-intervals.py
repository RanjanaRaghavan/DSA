class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort() 
        res = [intervals[0]]
        for i in range(len(intervals)-1):

            if res[-1][1] >= intervals[i+1][0]:
                res[-1][0] = min(res[-1][0] , intervals[i+1][0])
                res[-1][1] = max(res[-1][1], intervals[i+1][1])
            else:
                res.append(intervals[i+1])
        
        return res

                

        