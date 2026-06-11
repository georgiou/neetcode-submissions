class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s2 = ''.join(sorted(s))
            if not s2 in anagrams:
                anagrams[s2] = []
            anagrams[s2].append(s)
        return [v for v in anagrams.values()]        