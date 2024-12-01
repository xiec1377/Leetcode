class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        idx = 0
        for i in range(1, n+1):
            if n % i == 0:
                idx += 1
                if idx == k:
                    return i
        return -1
        

        