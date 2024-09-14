class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary = {}
        if not len(s) == len(t):
            return False
        for char in s:
            print(char)
            if char in dictionary.keys():
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        for char in t:
            print(char)
            if char in dictionary.keys():
                dictionary[char] -= 1
            else:
                return False
        
        for value in dictionary.values():
            if not value == 0:
                return False
        return True

        