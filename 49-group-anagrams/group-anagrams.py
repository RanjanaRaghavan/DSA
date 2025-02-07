class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = collections.defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return [v for v in anagrams.values()]
        