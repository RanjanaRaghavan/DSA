class Solution:
    
    #Helper func
    def ship(self,mid,weights):
        no_of_days = 0
        cur_weight = 0

        for weight in weights:
            if cur_weight + weight <= mid:
                cur_weight += weight
            else:
                no_of_days +=1
                cur_weight = weight
        
        if cur_weight > 0:
            no_of_days +=1

        return no_of_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        #Search Space
        low = max(weights)
        high = sum(weights)

        res = high

        #helper function to check feasibility
        #helper function returns the no od days u can ship with this capacity

        while (low <= high):

            mid = low + (high-low) // 2
            
            d = self.ship(mid,weights)

            if d <= days:
                res = min(mid,res)
                high = mid -1
            
            else:
                low = mid + 1
        
        return res



