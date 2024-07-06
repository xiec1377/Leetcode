class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums
        heapq.heapify(heap)

        for i in range(len(nums)-k):
            heapq.heappop(heap)
            # print("new heap:", heap)

        return heap[0]


        