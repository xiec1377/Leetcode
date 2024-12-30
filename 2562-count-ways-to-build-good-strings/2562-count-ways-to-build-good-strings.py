class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        dp = [0] * (high + 1)
        result = 0
        MOD = 10**9 + 7

        # base case: only 1 way to create "" string
        dp[0] = 1 
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i-zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i-one]) % MOD
            if i >= low:
                result = (result + dp[i]) % MOD
        return result
        