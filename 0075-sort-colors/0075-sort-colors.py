class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0 
        while slow < len(nums) and fast < len(nums) - 1:
            fast = slow + 1
            print("slow:", slow, "fast:", fast)
            if nums[slow] > nums[fast]:
                tmp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = tmp
                while slow > 0:
                    if nums[slow] < nums[slow-1]:
                        tmp = nums[slow]
                        nums[slow] = nums[slow-1]
                        nums[slow-1] = tmp
                    slow -= 1
                slow = fast
            else:
                slow += 1


        # arr = [0] * 3
        # res = []
        # for num in nums:
        #     arr[num] += 1
        # print("arr:", arr)

        # nums = []
        # for i in range(len(arr)):
        #     for j in range(arr[i]):
        #         nums.append(i)
        # print("nums:", nums)
        # return nums
        