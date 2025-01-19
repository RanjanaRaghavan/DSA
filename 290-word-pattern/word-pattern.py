class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split(' ')

        l1 = len(pattern)
        l2 = len(s)

        if l1 != l2:
            return False

        pat_to_s = collections.defaultdict(str)
        s_to_pat = collections.defaultdict(str)

        for i in range(l1):

            #pattern should not be in pattern map and should be check
            if pattern[i] not in pat_to_s:
                pat_to_s[pattern[i]] = s[i]
            else:
                if pat_to_s[pattern[i]] != s[i]:
                    return False
            
            if s[i] not in s_to_pat:
                s_to_pat[s[i]] = pattern[i]
            else:
                if s_to_pat[s[i]] != pattern[i]:
                    return False

        return True


        