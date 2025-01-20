class Solution:
    def climbStairs(self, n: int) -> int:


        #Dict to store steps
        '''
        key : step no
        value : no of ways
        '''

        ways_dict = collections.defaultdict(int)

        def no_of_ways(n):

            #Base Case
            if n ==1:
                return 1
            
            if n == 2:
                return 2
            
            if n in ways_dict:
                return ways_dict[n]
            else:
                ways_dict[n] = no_of_ways(n-1) + no_of_ways(n-2)
                return ways_dict[n]
                
        
        return no_of_ways(n)
        