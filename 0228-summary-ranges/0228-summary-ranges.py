class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # two pointers
        slow = 0
        fast = 0
        result = []
        while slow < len(nums) and fast < len(nums):
            if fast + 1 < len(nums) and nums[fast + 1] == nums[fast] + 1:
                fast += 1
            else:
                if nums[slow] == nums[fast]:
                    result.append(str(nums[slow]))
                else:
                    result.append(str(nums[slow]) + "->" + str(nums[fast]))
                fast += 1
                slow = fast
        return result


        
            

        