class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) > 1:
            return True
        dic = {}
        # for i, num in enumerate(arr):
        #     print("i:", i)
        #     print("num:", num)
        #     dic[i] = num
        
        # for key, val in dic.items():
        #     print("key:", key)
        #     print("val:", val)
        #     if i in dic.keys() and i != key and dic[i] == dic[key] * 2:
        #         print("we here")
        #         return True
        # return False

        for num in arr:
            dic[num] = num * 2
        print("dic:", dic)
        # if 0 in dic.keys():
        #     return True
        for key, val in dic.items():
            if key != val and (val in dic.keys() or key in dic.values()):
                return True
        return False
