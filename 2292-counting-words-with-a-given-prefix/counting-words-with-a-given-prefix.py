class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0
        for c in words:
            if c.startswith(pref):
                count +=1
        
        return count
        