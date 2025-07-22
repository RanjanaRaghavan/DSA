class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        '''
        Approach
        1. Check if both strings have the same letters repeating if not return empty
        2. Find GCD of the lengths and return
        '''
        '''
        Time Complexity : O(m+n) -> m = len(str1) n = len(str2)
        Space Complexity : O(m+n) -> m = len(str1) n = len(str2)
        '''

        if str1 + str2 != str2 +str1:
            return ''
        
        gcf = gcd(len(str1) , len(str2))

        return str1[0:gcf]

# def test_gcdOfStrings():

#     sol = Solution()

#     #min
#     assert sol.gcdOfStrings("A","A") == "A"
#     #max
#     assert sol.gcdOfStrings("ABC","ABCABC") == "ABC"
#     #same
#     assert sol.gcdOfStrings("ABC","ABC") == "ABC"
#     #regular
#     assert sol.gcdOfStrings("ABCABC","ABC") == "ABC"
#     #no op
#     assert sol.gcdOfStrings("LEET","CODE") == ""

# test_gcdOfStrings()
# print("All Tests passed")


        