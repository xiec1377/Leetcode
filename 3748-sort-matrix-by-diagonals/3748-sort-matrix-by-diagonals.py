class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        # bottom triangle
        for r in range(rows):
            diagonal = []
            for j in range(rows - r):
                diagonal.append(grid[r+j][j])
            diagonal.sort(reverse=True)
            for j in range(rows - r):
                grid[r+j][j] = diagonal[j]
        # top triangle
        for c in range(1, cols):
            diagonal = []
            for j in range(cols - c):
                diagonal.append(grid[j][c+j])
            diagonal.sort()
            for j in range(cols - c):
                grid[j][c+j] = diagonal[j]
        return grid
            
                
        