class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # O(nlogn)
        i = 0 
        res = []
        while i < len(nums) - 1:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
            i += 1
        return res
        