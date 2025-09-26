class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        print("max:", maxNum)
        slow, fast, maxInWindow = 0, 0, 0
        result = 0
        for fast in range(len(nums)):
            print("fast:", nums[fast])
            if nums[fast] == maxNum:
                maxInWindow += 1
            while maxInWindow >= k:
                if nums[slow] == maxNum:
                    maxInWindow -= 1
                slow += 1
            result += slow # increase by slow because slow index is smallest possible window so increasing it adds to the count 
        return result
        