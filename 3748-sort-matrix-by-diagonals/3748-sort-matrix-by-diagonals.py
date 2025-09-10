class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # bottom triangle
        for i in range(n):
            tmp = [grid[i+j][j] for j in range(n-i)]
            # print("tmp:", tmp)
            tmp.sort(reverse=True)
            for j in range(n - i):
                # print("j:", j)
                grid[i+j][j] = tmp[j]
        # top triangle
        for i in range(1, n): # don't include middle diagonal
            tmp = [grid[j][i+j] for j in range(n-i)]
            tmp.sort()
            for j in range(n-i):
                grid[j][i+j] = tmp[j]
        return grid
        