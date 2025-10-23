class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        def bfs(r, c):
            q = deque()
            start = (r, c)
            q.append((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            visited = set()
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for direction in directions:
                    newr = row + direction[0]
                    newc = col + direction[1]
                    if newr < 0 or newc < 0:
                        pacific.add((r, c))
                    if newr >= rows or newc >= cols:
                        atlantic.add((r, c))
                    if 0 <= newr < rows and 0 <= newc < cols and heights[newr][newc] <= heights[row][col] and (newr, newc) not in visited:
                        q.append((newr, newc)) 
                        visited.add((newr, newc))

        res = []
        for r in range(rows):
            for c in range(cols):
                bfs(r, c)
        return list(pacific & atlantic)

        