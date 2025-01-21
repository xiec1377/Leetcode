class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_top = sum(grid[0])
        sum_bot = 0
        result = float('inf')
        for i in range(len(grid[0])):
            sum_top -= grid[0][i]
            result = min(result, max(sum_top, sum_bot))
            sum_bot += grid[1][i]
        return result

        # Time complexity: O(2*n) = O(n)
        # Space complexity: O(1)
    