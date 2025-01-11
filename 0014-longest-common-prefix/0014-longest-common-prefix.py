class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # set the prefix as first word of strs
        prefix = strs[0] 
        for i, word in enumerate(strs):
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix
        