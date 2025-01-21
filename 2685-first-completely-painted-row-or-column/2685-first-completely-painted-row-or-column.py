class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        # keep map of each number in matrix mapped to value of (x, y) in matrix
        coords = {}
        for i in range(rows):
            for j in range(cols):
                coords[mat[i][j]] = (i, j)

        # keep hash map of which rows and cols are painted
        painted_rows = [0] * rows
        painted_cols = [0] * cols
        for idx, a in enumerate(arr):
            i, j = coords[a]
            painted_rows[i] += 1
            painted_cols[j] += 1
            if painted_rows[i] == cols or painted_cols[j] == rows:
                return idx
        return len(arr) - 1


        
        