class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        '''
            Find out max candy 
            loop thru every child and check if candy + extra > maxcandy
            fill result arry with boolean vals
        '''
        maxcandies = max(candies)
        result = [] 
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                result.append(True)
            else:
                result.append(False)
        
        return result



        
        