class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pref = strs[0]

        for c in strs:

            while not c.startswith(pref):
                pref = pref[:-1]
        
        return pref
        