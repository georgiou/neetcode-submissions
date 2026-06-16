class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq = [0]*26

        max_freq = 0
        max_len = 0

        for r, c in enumerate(s):
            rp = ord(c)-ord('A')
            freq[rp] += 1
            max_freq = max(freq[rp], max_freq)
            if r-l+1 - max_freq > k:
                lp = ord(s[l])-ord('A')
                freq[lp] -= 1
                l += 1
            max_len = max(max_len, r - l+ 1)

        return max_len