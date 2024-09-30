class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = float('-inf')
        while left < right:
            volume = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, volume)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxWater
        