class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

        def canDistribute(mid):
            stores = 0
            for q in quantities:
                stores += (q + mid - 1) // mid
            return stores <= n
        l = 1
        r = max(quantities)
        while l < r:
            mid  = (l+r) // 2
            if canDistribute(mid):
                r = mid
            else:
                l = mid + 1
        return l