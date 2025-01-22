class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr = 0
        
        while n != 0:
            ctr += 1
            n = n & (n-1)
        
        return ctr
        