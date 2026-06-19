class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frqS, frqT = {}, {}
        for i in range(len(s)):
            frqS[s[i]] = frqS.get(s[i], 0) + 1
            frqT[t[i]] = frqT.get(t[i], 0) + 1
        return frqS == frqT