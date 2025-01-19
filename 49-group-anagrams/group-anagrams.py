class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return [v for v in anagrams.values()]
