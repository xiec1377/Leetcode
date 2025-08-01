class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        myDict = defaultdict(int)
        arr = [0] * len(grid) ** 2
        print("len arr:", len(arr))
        row = len(grid)
        res = [0] * 2
        for i in range(row):
            for j in range(row):
                print("i:", i)
                print("j:", j)
                print(grid[i][j])
                arr[grid[i][j] - 1] += 1
                if arr[grid[i][j] - 1] >= 2:
                    print("grid[i][j]:", grid[i][j] - 1)
                    res[0] = grid[i][j]

        for i in range(len(arr)):
            if arr[i] == 0:
                res[1] = i + 1
                
        return res
        
        