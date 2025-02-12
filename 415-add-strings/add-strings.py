class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        l1 = len(num1) -1
        l2 = len(num2) -1

        carry = 0
        res = []

        while l1 >=0 or l2>=0:

            x = ord(num1[l1]) - ord('0') if l1>=0 else 0
            y = ord(num2[l2]) - ord('0') if l2>=0 else 0

            res.append((x + y + carry )%10)
            carry = (x + y + carry ) // 10

            l1 -= 1
            l2 -= 1
        
        if carry > 0:
            res.append(carry)
        
        return ''.join(str(s) for s in res[::-1])



        