class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = defaultdict(int)
        for i in range(len(nums)):
            for key in mydict.keys():
                if nums[i] == mydict[key]:
                    return [key, i]
            mydict[i] = target - nums[i]
        return []