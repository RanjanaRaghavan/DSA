class Solution:
    def repeatedCharacter(self, s: str) -> str:

        #Set to store unique chars
        unique_list = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            if unique_list[index] > 0:
                return char

            unique_list[index] = 1
        
        return -1
        