class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost_dict = collections.defaultdict(int)

        def min_cost(n):

            #basec case for below 0
            if n < 0:
                return 0 
            #base case 
            if n == 0 or n == 1:
                return 0
            
            #check cost_dict
            if n in cost_dict:
                return cost_dict[n]
            else:
                cost_dict[n] = min(min_cost(n-1) + cost[n-1], min_cost(n-2) + cost[n-2])
                return cost_dict[n]

        return min_cost(len(cost))


            

        