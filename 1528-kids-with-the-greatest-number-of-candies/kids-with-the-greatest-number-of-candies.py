class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        '''
            1. Find max candies
            2. loop thru the arr
            3. if candy + extracandies > max set to true else false
        '''

        output = []

        maxCandies = max(candies)
        
        for i in range(0,len(candies)):

            if candies[i] + extraCandies >= maxCandies:
                output.append(True)
            else:
                output.append(False)
        
        return output


        