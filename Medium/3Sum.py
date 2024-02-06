# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort nums
        nums.sort()
        # print("nums:", nums)
        answer = set()
        output = []
        for i in range(len(nums)):
            # print("i:", i)
            j = i + 1
            k = len(nums) - 1
            # print("j:", j)
            # print("k:", k)
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                # print("sum:", sum)
                if sum == 0:
                    # print("sum is 0")
                    answer.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif sum > 0:
                    # print("first sum is less than last")
                    k -= 1
                else:
                    # print("first sum is greater than last")
                    j += 1
        # print("answer:", answer)
        output = list(answer)
        return output

