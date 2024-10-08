class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for bracket in s:
            if bracket == '[':
                count += 1
            else:
                if count > 0:
                    count -= 1
        # + 1 to account for odd number, // 2 to do floor division bc min swaps is only half of max swaps
        return (count + 1) // 2 