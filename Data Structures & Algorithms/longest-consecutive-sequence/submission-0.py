class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                continue
            if num - 1 not in seen and num + 1 not in seen:
                seen[num] = 1
            else:
                left = seen.get(num - 1, 0)
                right = seen.get(num + 1, 0)
                length = left + right + 1

                seen[num] = length
                seen[num-left] = length
                seen[num+right] = length
        return max(seen.values(), default=0)