# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


class Solution(object):
    def dfs(self, grid, row, col): 
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
            grid[row][col] = 'x' #means visited
            self.dfs(grid, row+1, col)
            self.dfs(grid, row, col+1)
            self.dfs(grid, row-1, col)
            self.dfs(grid, row, col-1)
            # print("grid:", grid)
        else:
            return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = range(len(grid))
        cols = range(len(grid[0]))
        count = 0
        for r in rows:
            for c in cols:
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    count += 1
        return count


        

