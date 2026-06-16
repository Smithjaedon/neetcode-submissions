class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                num *= nums[j]
            arr.append(num)
        return arr
