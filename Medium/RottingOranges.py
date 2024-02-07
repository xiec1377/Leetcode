# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int 
        """
        rotten = deque()
        numFresh = 0
        minutes = 0
        # get all fresh oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    print("FRESH ORANGE", row, col)
                    numFresh += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))
        
        # no fresh oranges
        if numFresh == 0:
            return 0

        while rotten and numFresh > 0:
            minutes += 1
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                # print(r, c)
                for _r, _c in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    newr = r+_r
                    newc = c+_c
                    if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        rotten.append((newr, newc))
                        numFresh -= 1
        
        if numFresh == 0:
            return minutes
        else:
            return -1

        # runtime 36 ms
        # beats 35.94% of users
        


