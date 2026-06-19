class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen2 = {}
        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c]+=1
        for c in t:
            if c not in seen2:
                seen2[c] = 1
            else:
                seen2[c]+=1
        return seen == seen2