class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic and abs(dic[nums[i]] - i) <= k:
                return True
            dic[nums[i]] = i
        return False

        