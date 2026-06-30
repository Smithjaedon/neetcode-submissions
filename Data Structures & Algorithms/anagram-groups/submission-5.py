class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, s in enumerate(strs):
            SORT = "".join(sorted(s))
            if SORT not in seen:
                seen[SORT] = [s]
            else:
                seen[SORT].append(s)
        return [c for c in seen.values()]