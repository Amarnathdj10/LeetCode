class Solution:
    def maxArea(self, height: list[int]) -> int:

        left = 0
        right = len(height)-1

        maxWater = 0

        while left < right:

            currentWidth = right - left
            currentHeight = min(height[right],height[left])
            currentArea = currentHeight * currentWidth

            maxWater = max(maxWater, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater