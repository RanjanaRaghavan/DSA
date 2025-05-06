class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            intervals.append(newInterval)
        else:
            for i in range(len(intervals)):
                if newInterval[0] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                if i == len(intervals) -1:
                    intervals.append(newInterval)

        res = [intervals[0]]

        for i in range(1 , len(intervals)):

            if res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0] , intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res

                
        