class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
            comb -->[]
            remaining val -> target - whatever
        '''
        res = []

        def bt(remain,comb,start):

            if remain == 0:
                res.append(list(comb))
                return 
            elif remain < 0:
                return
            
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                bt(remain -candidates[i],comb,i)

                comb.pop()

        bt(target,[],0)
        return res