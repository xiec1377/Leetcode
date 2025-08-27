class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = 0
        while l <= r:
            mid = floor((l + r)/ 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return l


# nums = [1, 3, 5, 6, 9] , target = 10






            
            


        