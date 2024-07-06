class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        sumVowels = 0
        maxVowels = float('-inf')

        for i in range(k):
            if s[i] in vowels:
                sumVowels += 1
                maxVowels = max(maxVowels, sumVowels)
        if len(s) == k:
            return maxVowels
        for i in range(k, len(s)):
            if s[i] in vowels:
                sumVowels += 1
            if s[i-k] in vowels:
                sumVowels -= 1
            maxVowels = max(maxVowels, sumVowels)
        return maxVowels
                

        # abc
        # bci
        # cii
        # iii