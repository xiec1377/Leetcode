class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []

        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                    
                c = b + 1
                d = len(nums) - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        while c < d and nums[c] == nums[c + 1]:
                            c += 1

                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1

                        c += 1
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1
        
        return result