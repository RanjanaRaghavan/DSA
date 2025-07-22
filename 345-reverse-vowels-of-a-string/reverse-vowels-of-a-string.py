class Solution:
    def reverseVowels(self, s: str) -> str:

        '''
        Approach
        1. left and right pointers for the word
        2. loop till we find both left and right vowels and swap 
        3. Do this until left <= right then return word
        '''
        '''
        Time Complexity : O(s) -> s = len(s)
        Space Complexity : O(s) -> s = len(s)
        '''
        if len(s) <= 1:
            return s

        slist = list(s)
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s)-1

        while left < right:

            while left < right and slist[left] not in vowels:
                left +=1

            while left < right and slist[right] not in vowels:
                right -=1

            slist[left],slist[right] = slist[right],slist[left]

            left += 1
            right -=1
        
        return ''.join(slist)

# def test_reverseVowels():

#     sol = Solution()

#     #min
#     assert sol.reverseVowels("b") == "b"
#     #max
#     assert sol.reverseVowels("AeIoU") == "UoIeA"
#     #same
#     assert sol.reverseVowels("AAAaaa") == "aaaAAA"
#     #no op
#     assert sol.reverseVowels("bcvdr") == "bcvdr"
#     #regular
#     assert sol.reverseVowels("IceCreAm") == "AceCreIm"

# test_reverseVowels()
# print("All Tests passed!")



        