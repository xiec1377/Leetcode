class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r: int, c: int):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while q:
                row, col = q.popleft()
                for direction in directions:
                    newr = row + direction[0]
                    newc = col + direction[1]
                    if newr >= 0 and newr < rows and newc >= 0 and newc < cols and grid[newr][newc] == '1' and not (newr, newc) in visited:
                        visited.add((newr, newc))
                        q.append((newr, newc))
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not (r, c) in visited:
                    numIslands += 1
                    bfs(r, c)

       
        
        return numIslands
                

        
