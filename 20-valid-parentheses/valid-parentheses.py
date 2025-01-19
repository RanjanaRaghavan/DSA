class Solution:
    def isValid(self, s: str) -> bool:

        #Edge Cases
        if len(s) == 0:
            return True
        if len(s) %2 != 0:
            return False
        
        '''
        # Define a Dict of kV pairs of parantheses
         Key :opening bracket
         value :closing bracket
        '''
        paran_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
            }

        #Define a stack
        paran_stack = []

        #Loop through s
        for i in range(len(s)):

            # if opening bracket of any kind i will add to stack
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                paran_stack.append(s[i])

            #else then check if top Element in stack is value of the key 
            #if its is true pop the stack
            #else return false
            else:
                if len(paran_stack) > 0 and s[i] == paran_dict[paran_stack[-1]]:
                    paran_stack.pop()
                else:
                    return False

    #check if len(stack) is 0
    #if 0 return true
    #else Fasle

        
        return len(paran_stack) == 0
    


        