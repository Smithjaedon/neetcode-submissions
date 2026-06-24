class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                if val == 0:
                    tmp = [nums[i],nums[l],nums[r]]
                    res.add(tuple(tmp))
                    l += 1
                    r -= 1

        return [list(i) for i in res]