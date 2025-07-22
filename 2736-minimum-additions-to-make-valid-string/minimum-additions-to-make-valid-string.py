class Solution:
    def addMinimum(self, word: str) -> int:

        '''
        Approach
        1. two pointers for word and pattern "abc"
        2. if letters equal move on to next letter in word
        3. else move to next letter in pattern increment count
        4. reset pattern pointer after p2 >2 --> p2 =0
        5. return count
        '''
        '''
        Time Complexity : O(n) -> n = len(word)
        Space Complexity : O(1) -> constant space for "abc"
        '''

        count = 0
        p1 = 0
        p2 = 0
        pattern = "abc"

        while p1 < len(word):

            if word[p1] == pattern[p2]:
                p1+=1
            
            else:
                count +=1
            
            p2+=1
            if p2 > 2:
                p2 =0 
            
        
        return count + (3-p2 if p2!=0 else 0)

# def test_addMinimum():

#     sol = Solution()

#     #max
#     assert sol.addMinimum("abcbabc") == 2
#     #min
#     assert sol.addMinimum("b") == 2
#     #no op
#     assert sol.addMinimum("abc") == 0
#     #regular
#     assert sol.addMinimum("ab") == 1
#     #same
#     assert sol.addMinimum("aaa") == 6

# test_addMinimum()
# print("All tests passed!")



        