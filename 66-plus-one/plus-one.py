class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        '''
        1. We have to loop from back of the array
        2. Add 1 to unit digit
        3. If 9 -> make 0 and carry 1 to previous digit
        '''

        #Array for ans
        ans = []

        for i in range(len(digits)-1,-1,-1):

            print(i)
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            
            #If we reached end of loop
            if i == 0:
                digits.append(1)
                return digits[::-1]
        
            

                

        