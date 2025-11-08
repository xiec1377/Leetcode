class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):

            freq[s[i]] += 1
            curLen = i - j + 1
            # number of characters to change
            if curLen - max(freq.values()) > k:
                freq[s[j]] -= 1
                j += 1
            res = max(res, i - j+ 1)
        return res
                    

                    

        