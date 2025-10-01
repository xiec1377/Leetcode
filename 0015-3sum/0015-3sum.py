class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        result = []
        k = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum == 0:
                    triple = [nums[i], nums[j], nums[k]]
                    result.append(triple)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return result

        