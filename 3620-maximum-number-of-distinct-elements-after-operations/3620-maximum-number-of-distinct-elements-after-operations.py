class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        prev = float('-inf')
        res = 0 
        for num in nums:
            new_num = max(prev + 1, num - k) # minimize value to maximize range
            if new_num <= num + k:
                res += 1
                prev = new_num
        return res
        # not memory efficient
        # nums = sorted(nums)
        # prev = float('-inf')
        # distinct = set()
        # krange = [x for x in range(-k, k + 1)]
        # for num in nums:
        #     i = 0
        #     while i < len(krange) and num + krange[i] in distinct:
        #         i += 1
        #     if i >= len(krange):
        #         distinct.add(num)
        #         continue
        #     if num + krange[i] != prev:
        #         distinct.add(num + krange[i])
        #         prev = num + krange[i]
        #     else:
        #         prev = num
            
        # return len(distinct)



        