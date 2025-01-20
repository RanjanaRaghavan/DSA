class Solution:
    def repeatedCharacter(self, s: str) -> str:

        #Set to store unique chars
        unique_set = set()

        for char in s:
            if char in unique_set:
                return char
            
            unique_set.add(char)
        
        return -1
        