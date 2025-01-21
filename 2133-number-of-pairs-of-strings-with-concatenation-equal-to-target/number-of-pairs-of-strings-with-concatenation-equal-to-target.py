class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        '''
        Have a comp dict
        nums[i] : freq
        '''
        ways = 0
        comp_dict = collections.Counter(nums)
        
        for num in comp_dict.keys():

            #Find Complement 
            if target.startswith(num):
            # Extract the remaining part
                comp = target[len(num):]
            else:
                comp = ""

            if comp in comp_dict:
                if comp != num:
                   ways +=  comp_dict[comp] * comp_dict[num]
                else:
                    ways += comp_dict[comp] * (comp_dict[comp]-1)

            
        return ways
