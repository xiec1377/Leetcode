class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        myDict = defaultdict(int)
        arr = [0] * len(grid) ** 2
        row = len(grid)
        res = [0] * 2
        for i in range(row):
            for j in range(row):
                print(grid[i][j])
                arr[grid[i][j] - 1] += 1
                if arr[grid[i][j] - 1] >= 2:
                    res[0] = grid[i][j]

        for i in range(len(arr)):
            if arr[i] == 0:
                res[1] = i + 1
                
        return res
        
        