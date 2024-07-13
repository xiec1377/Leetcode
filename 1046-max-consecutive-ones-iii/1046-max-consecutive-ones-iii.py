class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        maxOnes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if k == 0:
                    while nums[start] != 0:
                        start += 1
                    start += 1
                else:
                    k -= 1
            maxOnes = max(maxOnes, i - start + 1)
        return maxOnes



        