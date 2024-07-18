class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        r = 0
        seqLen = 1
        maxSeq = float('-inf')
        
        while r < len(nums) - 1:
            if nums[r+1] == nums[r] + 1:
                seqLen += 1
                r += 1
            elif nums[r+1] == nums[r]:
                r += 1
            else:
                maxSeq = max(maxSeq, seqLen)
                seqLen = 1
                r += 1
        maxSeq = max(maxSeq, seqLen)
        return maxSeq