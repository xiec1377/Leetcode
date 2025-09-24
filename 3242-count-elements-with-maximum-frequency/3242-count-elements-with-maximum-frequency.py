class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maxFreq = 0
        result = 0
        for num in nums:
            freq[num] += 1
        for key in freq.keys():
            maxFreq = max(maxFreq, freq[key])

        for key in freq.keys():
            if freq[key] == maxFreq:
                result += freq[key]
        return result

