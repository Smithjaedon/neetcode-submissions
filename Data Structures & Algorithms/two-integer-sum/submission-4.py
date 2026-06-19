class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            need = target - v
            if need not in seen:
                seen[v] = i
            else:
                return [seen[need], i]
            
