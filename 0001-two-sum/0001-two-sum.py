class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary.keys():
                return [dictionary[nums[i]], i]
            dictionary[target - nums[i]] = i
        
        