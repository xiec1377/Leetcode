class Solution(object):
    def sum_array(self, arr):
        sum = 0
        for i in arr:
            sum += i
        return sum
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        sum = self.sum_array(nums)
        first_sum = 0
        for i in range(0, len(nums) - 1):
            first_sum += nums[i]
            if first_sum >= sum - first_sum:
                ans += 1
        return ans

        