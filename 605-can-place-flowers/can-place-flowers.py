class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        '''
            1. check adjacent cells and keep subtracting n till end of loop
            2. if n ==0 return true else false 

            0,1,0,0. n =1
            |
                |

        '''
        #base Case

        if n ==0 :
            return True

        if len(flowerbed) < n:
            return False

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n==1:
                return True
            elif flowerbed[0] == 1 and n ==0:
                return True
            else:
                return False
            
        for i in range(0,len(flowerbed)):

            #edge cases
            if i == 0:
                prevbed = 0
                nextbed = flowerbed[i+1]
            elif i == len(flowerbed) -1 :
                nextbed = 0
                prevbed = flowerbed[i-1]
            else:
                nextbed = flowerbed[i+1]
                prevbed = flowerbed[i-1]

            if flowerbed[i] == 0 and (flowerbed[i] == nextbed == prevbed):
                flowerbed[i] = 1
                n -=1
            
            if n == 0:
                return True

            i = i+2
    
        return n==0


