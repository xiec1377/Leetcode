# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution(object):
    def isVowel(self, c):
        char = c.lower()
        return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two pointers
        left = 0
        right = len(s) - 1
        str_list = list(s)
        while not left >= right:
            isVowelLeft = self.isVowel(str_list[left])
            isVowelRight = self.isVowel(str_list[right])
            if isVowelLeft and isVowelRight:
                buffer = str_list[left]
                str_list[left] = str_list[right]
                str_list[right] = buffer
                left += 1
                right -= 1
            elif not isVowelLeft and isVowelRight:
                left += 1  
            elif isVowelLeft and not isVowelRight:
                right -= 1
            else:
                left += 1
                right -= 1
        t = "".join(str_list)
        return t

        #runtime: O(n)
