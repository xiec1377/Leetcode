class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            if stack and ((char == 'B' and stack[-1] == 'A') or (char == 'D' and stack[-1] == 'C')):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
        