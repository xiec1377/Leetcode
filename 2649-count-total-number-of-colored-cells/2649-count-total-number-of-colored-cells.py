class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        res = 1
        res += 2  * n * (n - 1)
        return res
            
        # res = 5
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 5
        # for i in range(3, n + 1):
        #     res += 4 + ((i - 2) * 4)
        # return res


        