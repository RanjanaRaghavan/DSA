class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        maxcapacity = 0

        while left < right:

            width = right - left
            maxcapacity = max(maxcapacity ,min(height[right], height[left]) * width)

            if( height[left] <= height[right]):
                left +=1
            
            else:
                right -=1
        
        return maxcapacity
        

