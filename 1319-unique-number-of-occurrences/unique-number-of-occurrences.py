class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctrDict = collections.Counter(arr)
        
        #dupSet = set()

        # for freq in ctrDict.values():
        #     if freq in dupSet:
        #         return False
            
        #     dupSet.add(freq)

        # return True

        return (len(set(ctrDict.values())) == len(ctrDict.values()))