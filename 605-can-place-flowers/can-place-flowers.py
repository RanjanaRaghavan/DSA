class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        '''
        Approach
        Assumption : flowebed[-1] == flowerbed[l+1] == 0
        1. if i-1 and i+1 ==0 , then i =1 if i =1 then skip next spot and check i+2 and reduce n by 1
        2. else move on to next spot
        3. return boolean
        '''

        '''
        Time Complexity : O(f) -> f = len(flowerbed)
        Space Complexity : O(1)
        '''
                
        l = len(flowerbed)

        #Base Case:
        if n ==0:
            return True
        
        i = 0 

        while i < l:

            if flowerbed[i] == 0:

                empty_left = (i == 0 or flowerbed[i-1] == 0) 
                empty_right = (i == l-1 or flowerbed[i+1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] == 1
                    n -=1

                    if n == 0:
                        return True
                    
                    i+=2
                    continue

            i+=1
        
        return n == 0
        

# def test_canPlaceFlowers():

#     sol = Solution()

#     #max
#     assert sol.canPlaceFlowers([1,0,0,0,1],5) == False
#     #min
#     assert sol.canPlaceFlowers([0],1) == True
#     #same
#     assert sol.canPlaceFlowers([1,1,1,1,1],100) == False
#     #regular
#     assert sol.canPlaceFlowers([1,0,0,0,1],1) == True
#     #no op
#     assert sol.canPlaceFlowers([1,0,0,0,1],0) == True

# test_canPlaceFlowers()
# print("All Tests passed!")

        