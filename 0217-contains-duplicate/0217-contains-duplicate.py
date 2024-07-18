class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setNums = set()
        for num in nums:
            if num in setNums:
                return True
            else:
                setNums.add(num)
        return False
        