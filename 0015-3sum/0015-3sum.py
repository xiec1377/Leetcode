class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print("nums:", nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                # if nums[i] is duplicate
                continue
            j = i + 1
            k = len(nums) - 1
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res
        