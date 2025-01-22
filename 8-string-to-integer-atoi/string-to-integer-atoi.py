class Solution:
    def myAtoi(self, s: str) -> int:

        #trim leading white space
        s = s.lstrip()

        #If string is empty
        if len(s) == 0:
            return 0

        #check for negative number
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0
        #Loop thru num until we hit a non numeric character
        for char in s:
            print(char)
            if char.isnumeric():
                num = (num *10) + int(char)
            else:
                break
        
        if neg:
            num =  0 - num
        
        if num > (2 ** 31) -1:
            return (2 ** 31) -1
        elif num < (-2 ** 31):
            return (-2 ** 31)
        else:
            return num





        