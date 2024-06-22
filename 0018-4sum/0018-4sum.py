class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = set()
        for i in range(len(nums)):
            for j in range(len(nums) -1, 0, -1):
                # print "i", i, "j", j
                l = i + 1
                r = j - 1
                while l < r:
                    # print "l:", l, "r:", r
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    # print "sum:", sum
                    if sum < target:
                        # print "sum < target"
                        l += 1
                    elif sum > target:
                        # print "sum > target"
                        r -= 1
                    else:
                        # print "sum == target"
                        quad = tuple([nums[i], nums[l], nums[r], nums[j]])
                        results.add(quad)
                        r -= 1
                        l += 1
        return results


        