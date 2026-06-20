class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            counter = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                counter *= nums[j]
            arr.append(counter)
        return arr
