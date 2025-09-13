class Solution:
    def maxFreqSum(self, s: str) -> int:
        conMap = defaultdict(int)
        vowelMap = defaultdict(int)
        maxCon, maxVow = 0, 0
        for c in s:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c =='u':
                vowelMap[c] += 1
                maxVow = max(maxVow, vowelMap[c])
            else:
                conMap[c] += 1
                maxCon = max(maxCon, conMap[c])
        return maxCon + maxVow

        