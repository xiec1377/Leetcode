class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = ''
        # diagonal flipping technique - ensures every bit at position (i, i) is unique
        for i in range(len(nums)):
            if nums[i][i] == '0':
                result += '1'
            else:
                result +='0'
        return result
        # Time: O(n)
        # Space: O(1)
        