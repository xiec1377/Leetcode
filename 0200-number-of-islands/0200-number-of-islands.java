class Solution {
    public int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private int rows;
    private int cols;
    public int numIslands(char[][] grid) {
        int numislands = 0;
        rows = grid.length;
        cols = grid[0].length;
        Set<String> visited = new HashSet<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                String pos = r + ", " + c;
                if (grid[r][c] == '1' && !visited.contains(pos)) {
                    numislands++;
                    bfs(grid, r, c, visited);
                }
            }
        }
        return numislands;

    }

    private void bfs(char[][] grid, int r, int c, Set<String> visited) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r, c});

        while (!q.isEmpty()) {
            int[] coord = q.poll();
            int row = coord[0];
            int col = coord[1];
            for (int[] direction : directions) {
                int newr = row + direction[0];
                int newc = col + direction[1];
                if (newr >= 0 && newr < rows && newc >= 0 && newc < cols && grid[newr][newc] == '1' && !visited.contains(newr + ", " + newc)){
                    q.add(new int[]{newr, newc});
                    visited.add(newr + ", " + newc);
                }
            }
        }
        
    }
}