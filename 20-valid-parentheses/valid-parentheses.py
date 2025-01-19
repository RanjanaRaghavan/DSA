class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) %2 != 0:
            return False
        
        #Stack to store the open parantheses
        paranStack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i]=='{':
                paranStack.append(s[i])
            else:
                if(len(paranStack) > 0):
                    topEle = paranStack[len(paranStack)-1]
                else:
                    return False
    
                if (s[i] == ')' and topEle == '(') or (s[i] == ']' and topEle == '[') or (s[i] == '}' and topEle == '{'):
                    paranStack.pop()
                else :
                    return False
        
        if len(paranStack) == 0:
            return True
        else:
            return False


        