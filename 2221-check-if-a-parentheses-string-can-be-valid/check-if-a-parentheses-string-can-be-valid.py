class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """

        if len(s) %2 !=0:
            return False
        
        s_open = 0
        s_close = 0
        oc = 0

        # Left to right scan
        for i in range(len(s)):
            if locked[i] == '0':
                oc += 1
            else:
                if s[i] == '(':
                    s_open += 1
                else:
                    s_close += 1

            if s_close > s_open + oc:  # Too many ')'
                return False
        
        #Right to left 
        s_open = 0
        s_close = 0
        oc = 0
        
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':  
                oc += 1
            elif s[i] == ')':
                s_close += 1
            else:
                s_open += 1

            if s_open > s_close + oc:
                return False  

        return True

                
            

        