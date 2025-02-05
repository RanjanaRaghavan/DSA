class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        res = []
        carry =0

        l1 = len(num1) -1
        l2 = len(num2) -1

        while l1 >=0 or l2 >=0:

            x1 = ord(num1[l1]) - ord('0') if l1 >=0 else 0
            x2 = ord(num2[l2]) - ord('0') if l2 >=0 else 0

            res.append((x1 + x2 + carry) %10)
            carry = (x1+x2 + carry) // 10

            l1 -=1
            l2 -=1

        if carry > 0:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])


        