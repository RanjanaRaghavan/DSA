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
            
        for i in range(0,len(flowerbed)):

            if flowerbed[i] == 0 and \
            (i==0 or flowerbed[i-1]==0) and \
            (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -=1
            
            if n == 0:
                return True

            i = i+2
    
        return n==0


