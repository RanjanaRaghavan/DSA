class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack1 = []

        for c in s:
            if stack1 and stack1[-1] == c:
                stack1.pop()
            else:
                stack1.append(c)
        
        return ''.join(stack1)
        