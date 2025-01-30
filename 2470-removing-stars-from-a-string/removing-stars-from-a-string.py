class Solution:
    def removeStars(self, s: str) -> str:

        star_stack = []

        for char in s:

            if char == '*':
                if len(star_stack) > 0:
                    star_stack.pop()

            else:
                star_stack.append(char)
        
        return ''.join(star_stack)