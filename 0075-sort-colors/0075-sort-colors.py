class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0 
        while slow < len(nums) and fast < len(nums) - 1:
            fast = slow + 1
            if nums[slow] > nums[fast]:
                tmp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = tmp
                while slow > 0:
                    if nums[slow] < nums[slow-1]:
                        tmp = nums[slow]
                        nums[slow] = nums[slow-1]
                        nums[slow-1] = tmp
                    slow -= 1
                slow = fast
            else:
                slow += 1