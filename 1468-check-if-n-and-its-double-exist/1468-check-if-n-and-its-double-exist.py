class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) > 1:
            return True
        seen = set()
        for num in arr:
            if num * 2 in seen or float(num) / 2 in seen:
                return True
            seen.add(num)
        return False


