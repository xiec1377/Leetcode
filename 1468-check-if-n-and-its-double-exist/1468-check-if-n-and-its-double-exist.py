class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) > 1:
            return True
        dic = {}
        for num in arr:
            dic[num] = num * 2
        print("dic:", dic)
        for key, val in dic.items():
            if key != val and (val in dic.keys() or key in dic.values()):
                return True
        return False
