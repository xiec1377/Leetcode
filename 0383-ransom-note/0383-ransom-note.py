from collections import defaultdict 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = defaultdict(int)

        for letter in magazine:
            if dic[letter]:
                dic[letter] += 1
            else:
                dic[letter] = 1

        for letter in ransomNote:
            if dic[letter] >= 1:
                dic[letter] -= 1
            else:
                return False
        return True
