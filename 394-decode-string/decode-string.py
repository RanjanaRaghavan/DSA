class Solution:
    def decodeString(self, s: str) -> str:

        stack1 = []

        for c in s:

            alpha = ''
            nums = ''

            if c != ']':
                stack1.append(c)
            
            else:
                while stack1 and stack1[-1] != '[' :
                    alpha = stack1.pop() + alpha
                
                #remove open bracket
                stack1.pop()
                
                while stack1 and stack1[-1].isnumeric():
                    nums = stack1.pop() + nums
                
                stack1.append(alpha * int(nums))
            
        
        return ''.join(stack1)



                

        