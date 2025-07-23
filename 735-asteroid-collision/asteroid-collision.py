class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''
        Approach
        1. Add first element to the result array
        2. if pos add to stack , if negative run a while loop till empty or gets destroyed
            a. -ve <---- , pos ----> so any -ve in front dont matter.
        3. return res array
        '''
        '''
        Time Complexity : O(n) n-> len(asteroids)
        Space Complexity : O(n) --> worst case no collisions
        '''
        res =[]
        for i in range(0,len(asteroids)):
            if asteroids[i] >= 0:
                res.append(asteroids[i])
            else:
                if len(res) == 0 or res[-1] < 0:
                    res.append(asteroids[i])
                else:
                    while res and res[-1] >=0:
                        #equal
                        if abs(res[-1]) == abs(asteroids[i]):
                            res.pop()
                            break
                        #small
                        elif abs(res[-1]) < abs(asteroids[i]):
                            res.pop()
                        else:
                            break
                    else:
                        res.append(asteroids[i])
            
        return res

# def test_asteroidCollision():

#     sol = Solution()
#     #reg
#     assert sol.asteroidCollision([5,10,-5]) == [5,10]
#     #min
#     assert sol.asteroidCollision([5,-5]) == []
#     #max
#     assert sol.asteroidCollision([300,4,3,4,-5]) == [300]
#     #no op
#     assert sol.asteroidCollision([5,10]) == [5,10]
#     #same
#     assert sol.asteroidCollision([5,5,5]) == [5,5,5]

# test_asteroidCollision()
# print("All tests passed!")


        