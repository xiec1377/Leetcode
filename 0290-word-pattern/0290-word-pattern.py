class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_arr = s.split(" ")
        print s_arr
        dic1 = {}
        dic2 = {}
        if len(s_arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            if (pattern[i] in dic1 and dic1[pattern[i]] != s_arr[i]) or (s_arr[i] in dic2 and dic2[s_arr[i]] != pattern[i]):
                return False
            if pattern[i] not in dic1:
                dic1[pattern[i]] = s_arr[i]
            if s_arr[i] not in dic2:
                dic2[s_arr[i]] = pattern[i]
        return True
            
            