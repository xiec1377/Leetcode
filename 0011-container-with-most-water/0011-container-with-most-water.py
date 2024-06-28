class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxVolume = float('-inf')
        l = 0
        r = len(height) - 1
        while l < r:
            volume = min(height[l], height[r]) * (r - l)
            if volume > maxVolume:
                maxVolume = volume
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxVolume
        