class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        res = 0
        while left < right:
            if maxLeft >= maxRight:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
            else:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
        return res