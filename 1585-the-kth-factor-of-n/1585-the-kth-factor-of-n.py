class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # list of factors
        # factors = []
        # for i in range(1, n+1):
        #     if n % i == 0:
        #         factors.append(i)
        
        # if 1 <= k <= len(factors):
        #     return factors[k-1]
        # else:
        #     return -1
        idx = 0
        for i in range(1, n+1):
            if n % i == 0:
                idx += 1
                if idx == k:
                    return i
        return -1
        

        