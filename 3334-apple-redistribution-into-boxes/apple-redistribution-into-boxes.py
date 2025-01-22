class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        total_apples = sum(apple)
        ctr = 0

        capacity.sort()

        capacity_sum = 0
        for c in capacity[::-1]:
            ctr +=1
            capacity_sum += c
            if capacity_sum >= total_apples:
                return ctr
        
        return -1

             
        