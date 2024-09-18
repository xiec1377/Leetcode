class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
        