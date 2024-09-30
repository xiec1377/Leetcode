class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
    
        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif red <= i < red + white:
                nums[i] = 1
            else:
                nums[i] = 2

            
