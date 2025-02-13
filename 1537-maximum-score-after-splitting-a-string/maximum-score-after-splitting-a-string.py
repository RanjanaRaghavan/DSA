class Solution:
    def maxScore(self, s: str) -> int:

        ones = 0
        zeroes = 0

        score = -inf

        for i in range(len(s)-1):
            if s[i] == '0':
                zeroes +=1
            else:
                ones +=1
            
            score = max(zeroes - ones,score)
        
        if s[-1] =='1':
            ones +=1
        
        return score + ones
        