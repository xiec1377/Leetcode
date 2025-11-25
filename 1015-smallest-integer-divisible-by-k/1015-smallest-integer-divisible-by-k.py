class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        remainder = 0
        for i in range(1, k+1):
            remainder = (remainder * 10 + 1) % k
            print("remainder:", remainder)
            if remainder == 0:
                return i
        return -1
        
        