class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] = 1 + frequency[num]
        arr = [[] for i in range(len(nums) + 1)]
        for key, val in frequency.items():
            arr[val].append(key)
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                if len(res) < k:
                    res.append(num)
        return res
        