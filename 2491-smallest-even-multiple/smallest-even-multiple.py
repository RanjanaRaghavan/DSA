class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        '''
        1. If n is odd -> then n *2 can only be smallest
        2. If n is even -> then that number itself is a multiple of both 2 and itself
        '''
        
        return n*2 if n%2 !=0 else n

def test_smallestEvenMultiple():

    sol = Solution()

    assert sol.smallestEvenMultiple(5) == 10
    assert sol.smallestEvenMultiple(6) == 6
    assert sol.smallestEvenMultiple(15) == 30
    assert sol.smallestEvenMultiple(22) == 22
    assert sol.smallestEvenMultiple(278) == 278

test_smallestEvenMultiple()
print("All tests passed!")

