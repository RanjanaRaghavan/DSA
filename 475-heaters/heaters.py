class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        i,j,maxRadius = 0,0,0

        while i < len(houses):
            while j < len(heaters)-1 and abs(heaters[j+1] - houses[i]) <= abs(heaters[j] - houses[i]):
                j+=1
            
            maxRadius = max(maxRadius, abs(heaters[j] - houses[i]))
            i+=1
        
        return maxRadius
        