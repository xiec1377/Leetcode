class Solution(object):

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final = ""
        i = 0
        while i < len(word1) and i < len(word2):
            final += word1[i]
            final += word2[i]
            i += 1
       # print("i: ", i)
        if len(word1) == len(word2):
            return final
        elif i == len(word1):
            # word2 is longer
            final += word2[i:len(word2)]
            #print("final:", final)
            return final
        else:
            # word1 is longer
            final += word1[i:len(word1)]
            return final
