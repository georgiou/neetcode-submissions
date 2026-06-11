class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = 26 * [0]
            for c in s:
                count[ord(c)-ord('a')] += 1
            s2 = tuple(count)
            anagrams[s2].append(s)
        return [v for v in anagrams.values()]        