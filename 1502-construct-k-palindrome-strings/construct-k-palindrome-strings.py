class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        #Base case
        if len(s) < k:
            return False

        ctr = Counter(s)
        odd = 0

        for val,freq in ctr.items():
            if freq %2 !=0:
                odd +=1

        if odd > k:
            return False
        else:
            return True




        

        