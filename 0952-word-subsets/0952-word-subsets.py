class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        freq = {}
        ans = []
        for wordb in words2:
            for c, n in Counter(wordb).items():
                if c not in freq.keys() or freq[c] < n:
                    freq[c] = n

        for worda in words1:
            isUniversal = True
            count = Counter(worda)
            for c, n in freq.items():
                if count[c] < n:
                    isUniversal = False
            if isUniversal:
                ans.append(worda)
        return ans