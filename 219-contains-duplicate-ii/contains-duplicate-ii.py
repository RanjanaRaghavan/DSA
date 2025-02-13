class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map1 = collections.defaultdict(int)

        for i,n in enumerate(nums):
            if n in map1 and abs(map1[n] - i) <=k:
                return True
            
            map1[n] = i
        
        return False
        