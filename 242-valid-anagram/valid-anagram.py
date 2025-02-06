class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map1 = collections.Counter(s)
        map2 = collections.Counter(t)

        for k,v in map1.items():
            if k not in map2:
                return False
            else:
                if map1[k] != map2[k]:
                    return False
        
        return True


        