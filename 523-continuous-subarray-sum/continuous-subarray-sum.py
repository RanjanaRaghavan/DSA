class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        '''
        1. Calculate prefix sum at every idx
        2. Do Sum % k
        3. input that in hashtable
            key -> remainer
            value -> idx
        4. If duplicate entry return True
        5. Comes out of loop return False
        '''
        map1 = {0:-1}
        prefix_sum = 0
        
        for i,n in enumerate(nums):

            prefix_sum += n
            r = prefix_sum % k

            if r in map1:
                if i - map1[r] > 1:
                    return True
            
            else:
                map1[r] = i
        
        return False
            

           
        




        