class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = float('-inf')
        zero, all_ones = 0, 0
        # count all 1s
        for char in s:
            if char == '1':
                all_ones += 1
        for i in range(len(s) - 1):
            if s[i] == '0':
                print("0")
                zero += 1
            else:
                print("1")
                all_ones -= 1
            max_score = max(max_score, zero + all_ones)
            print("max_score:", max_score)
        return max_score

        
        