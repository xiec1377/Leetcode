class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        for i in range(0, len(s)):
            if s[i] in dic.keys():
                res += 1
                dic.clear()
            dic[s[i]] = True
        res += 1
        return res

        