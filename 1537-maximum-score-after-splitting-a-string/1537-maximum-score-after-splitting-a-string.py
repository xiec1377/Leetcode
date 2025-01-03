class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = float('-inf')
        zero, one = 0, 0
        all_zeros, all_ones = 0, 0
        for char in s:
            if char == '0':
                all_zeros += 1
            if char == '1':
                all_ones += 1
        print("All zoers:", all_zeros)
        print("all ones:", all_ones)
        for i in range(len(s) - 1):
            if s[i] == '0':
                print("0")
                zero += 1
                all_zeros -= 1
            else:
                print("1")
                one += 1
                all_ones -= 1
            max_score = max(max_score, zero + all_ones)
            print("max_score:", max_score)
        return max_score

        
        