class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS, seenT = {}, {}
        for c in s:
            seenS[c] = seenS.get(c, 0) + 1
        for c in t:
            seenT[c] = seenT.get(c, 0) + 1
        return seenS == seenT
