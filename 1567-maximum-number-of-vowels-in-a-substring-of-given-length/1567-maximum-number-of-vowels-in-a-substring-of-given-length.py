class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # sliding window probelm
        # keep track of beginning of window
        # iterate through char in s
        # keep track of max vowels

        vowels = ['a', 'e', 'i', 'o', 'u']
        sumVowels = 0
        maxVowels = float('-inf')

        for i in range(k):
            # print("iii:", i)
            if s[i] in vowels:
                sumVowels += 1
                maxVowels = max(maxVowels, sumVowels)
            
        
        # print("maxvowels", maxVowels)
        if len(s) == k:
            return maxVowels

        start = 1
        for i in range(k, len(s)):
            # print("char:", s[i])
            if s[i] in vowels:
                sumVowels += 1
            if s[i-k] in vowels:
                sumVowels -= 1
            # print("sumvowels", sumVowels)
            maxVowels = max(maxVowels, sumVowels)

            # print("max:", maxVowels)
            # start += 1
        return maxVowels
                

        # abc
        # bci
        # cii
        # iii