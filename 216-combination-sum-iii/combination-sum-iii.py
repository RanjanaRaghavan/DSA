class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def bt(remain,comb,start):

            if remain == 0 and len(comb) == k:
                res.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return

            for i in range(start,9):
                comb.append(i+1)
                bt(remain-i -1,comb,i+1)

                comb.pop()

        bt(n,[],0)
        return res
        