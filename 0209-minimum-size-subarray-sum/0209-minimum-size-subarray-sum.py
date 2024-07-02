class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum = 0
        minLen = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                print("thing:", i, start)
                minLen = min(minLen, i - start + 1)
                sum -= nums[start]
                start += 1
        if minLen != float('inf'):
            return minLen
        else:
            return 0




        