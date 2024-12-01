class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        seen = set()
        l = 0
        res = 0
        seen.add(s[l])
        for i in range(1, len(s)):
            if s[i] in seen:
                l = i
                set.clear(seen)
                res += 1
            seen.add(s[i])
        
        res += 1
        return res

        