class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ans = 0
        for word in words:
            print("word[0:len(pref)]:", word[0:len(pref)] )
            if word[0:len(pref)] == pref:
                ans += 1
        return ans
        