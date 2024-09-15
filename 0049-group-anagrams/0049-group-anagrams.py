class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramDic = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            if tuple(count) in anagramDic.keys():
                anagramDic[tuple(count)].append(s)
            else:
                anagramDic[tuple(count)] = [s]
        return anagramDic.values()