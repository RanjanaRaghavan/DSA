class Solution:
    def reverseBits(self, n: int) -> int:
        res =0
        power = 31 #bcuz 32 bit int and index starts from 0

        while n:
            res += (n & 1) << power
            n = n >> 1
            power -=1

        return res