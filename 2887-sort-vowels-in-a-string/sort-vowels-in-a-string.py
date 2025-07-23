class Solution:
    def sortVowels(self, s: str) -> str:

        '''
        Approach
        1. Add all vowels into a new array and sort
        2. traverse thru string and add a vowel from new array to replace this
        3. return new string
        '''
        '''
        Time Complexity: O(s log t) s-->len(s) t-->len(t) for sorting
        Space Complexity: O(n) -> worst case all are vowels
        '''

        vowels = "AEIOUaeiou"
        vowel_list = []
        for c in s:
            if c in vowels:
                vowel_list.append(c)
        
        if not vowel_list:
            return s
        else:
            vowel_list.sort()
            t = []
            i = 0
            for c in s:
                if c not in vowels:
                    t.append(c)
                else:
                    t.append(vowel_list[i])
                    i+=1
        
        return ''.join(t)

def test_sortVowels():

    sol = Solution()

    assert sol.sortVowels("lEetcOde") == "lEOtcede"
    assert sol.sortVowels("lEetcOde") == "lEOtcede"
    assert sol.sortVowels("lEetcOde") == "lEOtcede"
    assert sol.sortVowels("lEetcOde") == "lEOtcede"
    






        