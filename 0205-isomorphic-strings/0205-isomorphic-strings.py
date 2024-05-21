class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        idx = 0
        while idx < len(s):
            if s[idx] not in dic1:
                dic1[s[idx]] = t[idx]
            else:
                if dic1[s[idx]] != t[idx]:
                    return False
            if t[idx] not in dic2:
                dic2[t[idx]] = s[idx]
            else:
                if dic2[t[idx]] != s[idx]:
                    return False
            idx += 1
        return True
            


        