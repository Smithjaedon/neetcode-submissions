class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, v in enumerate(strs):
            letters = "".join(sorted(v))
            if letters not in seen:
                seen[letters] = [strs[i]]
            else:
                seen[letters].append(strs[i])
        return list(seen.values())
        

            