class Solution:
    def isValid(self, s: str) -> bool:

        #Edge Case
        if len(s) == 0:
            return False

        if len(s) %2 == 1:
            return False

        map1 = {
            '(' :')',
            '{' :'}',
            '[' : ']'
        }
        stack1 = []

        for c in s:
            if c in map1:
                stack1.append(c)
            else:
                if stack1 and map1[stack1[-1]] == c:
                    stack1.pop()
                else:
                    return False
        
        return len(stack1) == 0


