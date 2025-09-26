class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        for k in range(len(nums)-1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    result += (j - i) # all other triplets in between 
                    j -= 1
                else:
                    i += 1
        return result

        