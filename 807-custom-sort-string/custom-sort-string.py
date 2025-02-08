class Solution:
    def customSortString(self, order: str, s: str) -> str:

        '''
        1. Have a ctr map for s
        2. Iterate through order and add the char * freq to result str
        '''

        if len(s) <= 1:
            return s
        
        ctr = Counter(s)
        res = ''
        
        for c in order:
            if c in ctr:
                res += (c * ctr[c])
                ctr[c] = 0
        
        for k,v in ctr.items():
            res += (k * v)

        return res

        