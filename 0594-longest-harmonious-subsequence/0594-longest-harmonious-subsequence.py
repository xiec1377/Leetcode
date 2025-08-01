class Solution:
    def findLHS(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        print("sortedNums:", sortedNums)
        if len(nums) == 1:
            return 0
        l = 0
        r = 1
        longest = float('-inf')
        while r < len(nums):
            print("l:", nums[l], "r:", nums[r])
            if sortedNums[r] - sortedNums[l] == 1:
                longest = max(longest, r - l + 1)
                r += 1
                print("longest:", longest)
            elif sortedNums[r] - sortedNums[l] < 1:
                r += 1
            else:
                l += 1

        if not longest == float('-inf'):
            return longest
        else:
            return 0
        