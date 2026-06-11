class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join( f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            sz = int(s[i:j])
            res.append(s[j+1:j+sz+1])
            i=j+sz+1
        return res