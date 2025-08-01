class Solution:
    def findLHS(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        if len(nums) == 1:
            return 0
        l = 0
        r = 1
        longest = float('-inf')
        while r < len(nums):
            if sortedNums[r] - sortedNums[l] == 1:
                longest = max(longest, r - l + 1)
                r += 1
            elif sortedNums[r] - sortedNums[l] < 1:
                r += 1
            else:
                l += 1
        if not longest == float('-inf'):
            return longest
        else:
            return 0
        