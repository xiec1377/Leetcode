class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0 
        r = len(nums) - 1
        i = len(nums) - 1
        result = [0] * (len(nums))
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                result[i] = nums[r] ** 2
                r -= 1
            else:
                result[i] = nums[l] ** 2
                l += 1
            i -= 1
        return result
        