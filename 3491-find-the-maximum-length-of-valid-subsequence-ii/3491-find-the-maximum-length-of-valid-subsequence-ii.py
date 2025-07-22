class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # initialize empty 2D dp matrix
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            curr = num % k 
            for prev in range(k): # try comparing current num with all possible previous values (0 -(k-1))
                dp[curr][prev] = dp[prev][curr] + 1 # length of current num with previous prev is just length of previous prev with current num + 1 
                res = max(res, dp[curr][prev])
        return res

