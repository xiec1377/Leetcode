class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows  = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = []
        res = 0

        def bfs(r, c):
            q = deque()
            q.append(((r, c), 1))
            visited.append((r, c))
            area = 1
            while q:
                item = q.popleft()
                row, col = item[0][0], item[0][1]
                size = item[1]
                for x, y in directions:
                    newr = row + x
                    newc = col + y
                    if 0 <= newr < rows and 0 <= newc < cols and grid[newr][newc] == 1 and (newr, newc) not in visited:
                        visited.append((newr, newc))
                        q.append(((newr, newc), size + 1))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    newmaxisland = bfs(r, c)
                    res = max(newmaxisland, res)
        
        return res


            

        