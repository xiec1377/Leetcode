class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        for char in s:
            if char != "*":
                string += char
            else:
                string = string[:-1]
        return string
