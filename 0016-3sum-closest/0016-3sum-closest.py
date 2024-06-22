class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort nums array first
        nums.sort()
        # two pointers
        smallestSum = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            # print "in", i, l, r
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                # print "sum:", sum
                diff = abs(target - sum)
                smallestDiff = abs(target - smallestSum)
                if diff < smallestDiff:
                    smallestSum = sum
                    smallestDiff = diff
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    break
        return smallestSum

        