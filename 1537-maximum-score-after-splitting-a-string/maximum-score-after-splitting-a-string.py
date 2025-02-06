class Solution:
    def maxScore(self, s: str) -> int:

        slist = list(map(int, s))
        
        total = sum(slist)

        #initial Calc
        if slist[0] == 0:
            left = 1
            right = total
        else:
            left =0
            right = total -1
        
        score = left + right
        
        for i in range(1,len(slist)-1):

            if slist[i] == 0:
                left += 1
            else:
                right -= 1

            score = max(score, left+right)
        
        return score




        
        