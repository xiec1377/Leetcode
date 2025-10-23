class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        def bfs(r, c):
            q = deque()
            start = (r, c)
            q.append((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            visited = set()
            visited.add((r, c))
            isPacific = False
            isAtlantic = False

            while q:
                row, col = q.popleft()
                for direction in directions:
                    newr = row + direction[0]
                    newc = col + direction[1]
                    if newr < 0 or newc < 0:
                        isPacific = True
                    if newr >= rows or newc >= cols:
                        isAtlantic = True
                    if 0 <= newr < rows and 0 <= newc < cols and heights[newr][newc] <= heights[row][col] and (newr, newc) not in visited:
                        q.append((newr, newc)) 
                        visited.add((newr, newc))
            if isPacific and isAtlantic:
                return True
            return False

        res = []
        for r in range(rows):
            for c in range(cols):
                canFlow = bfs(r, c)
                if canFlow:
                    res.append((r, c))
        return res

        