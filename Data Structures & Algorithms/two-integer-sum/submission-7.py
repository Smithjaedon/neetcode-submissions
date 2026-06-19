class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            needed = target - v
            if needed not in seen:
                seen[v] = i
            else:
                return [seen[needed], i]
        return []
