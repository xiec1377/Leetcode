class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        res = 1
        res += 2  * n * (n - 1)
        return res
            


        