class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSum = float('-inf')
        l,r = 0, len(heights) - 1
        while l < r:
            sum = (r-l) * min(heights[l], heights[r]) 
            if sum > maxSum:
                maxSum = sum
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxSum