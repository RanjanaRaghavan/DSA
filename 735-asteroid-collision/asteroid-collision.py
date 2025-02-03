class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''
        1. It only matters if the asteroid is negative that comes from the right
        2.if its positive directly add to stack
        3. if negative, then run a while loop till the asteroid becomes smaller than previous

        '''

        stack1 = []

        for a in asteroids:

            if a > 0:
                stack1.append(a)

            else:

                if len(stack1) > 0 and stack1[-1] < 0:
                    stack1.append(a)
                else:
                    while len(stack1) > 0 and (stack1[-1] >0  and abs(a) > stack1[-1]):
                        stack1.pop()
                        #print(a,stack1)

                    if len(stack1) == 0:
                        stack1.append(a)
                    elif stack1[-1] >0 and abs(a) == stack1[-1]:
                        stack1.pop()
                        continue
                    elif len(stack1) > 0 and stack1[-1] < 0:
                        stack1.append(a)
                    else:
                        continue
            #print(stack1)

        return stack1



        