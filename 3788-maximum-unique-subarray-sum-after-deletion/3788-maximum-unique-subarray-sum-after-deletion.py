class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            if num > 0:
                mySet.add(num)
            
        if len(mySet) > 0:
            return sum(mySet)
        else:
            return max(nums)
        



        