class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        right = len(nums) -1
        left = 0
        sums = nums[right] + nums[left]
        if sums == target:
            return [left, right]
        for i in range(len(nums)):
            left = i
            #print "left: ", left
            for j in range(len(nums) - 1 - i):
                right = i + 1 + j
                #print "right: ", right
                sums = nums[right] + nums[left]
                if sums == target:
                    return [left, right]
