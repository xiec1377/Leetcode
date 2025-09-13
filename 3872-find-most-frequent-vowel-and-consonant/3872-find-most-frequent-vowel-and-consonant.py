class Solution:
    def maxFreqSum(self, s: str) -> int:
        conMap = defaultdict(int)
        vowelMap = defaultdict(int)
        maxCon = float('-inf')
        maxVow = float('-inf')
        for c in s:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c =='u':
                vowelMap[c] += 1
                maxVow = max(maxVow, vowelMap[c])
            else:
                conMap[c] += 1
                maxCon = max(maxCon, conMap[c])
            
        if maxCon == float('-inf'):
            maxCon = 0
        if maxVow == float('-inf'):
            maxVow = 0
        return maxCon + maxVow

        