class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr = 0
        mask = 1

        for i in range(0,32):
            if n & mask != 0:
                ctr += 1
            
            mask = mask << 1
        
        return ctr
        