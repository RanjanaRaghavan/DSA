class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:

        rem_ctr = collections.Counter()

        for n in nums:
            reminder = n % space
            rem_ctr[reminder] +=1
        
        max_count = 0
        for count in rem_ctr.values():
            max_count = max(max_count,count)
        
        min_value = float("inf")
        for n in nums:
            if rem_ctr[n%space] == max_count:
                if n < min_value:
                    min_value = n
        
        return min_value

        