class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minr, maxr = rows, -1
        minc, maxc = cols, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)
        height = maxr - minr + 1
        width = maxc - minc + 1
        return width * height


        