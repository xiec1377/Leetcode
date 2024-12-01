class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top, bottom = 0, len(matrix) - 1
        # do binary search on beginning int in rows
        while top <= bottom:
            mid = (top + bottom) // 2
            print("mid of rows:", mid)
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        #if we can't find one mid means target doesn't exist
        if not (top <= bottom):
            return False
        mid = (top + bottom) // 2
        
        # do binary search on mid row
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            mid2 = (l + r) // 2
            if target > matrix[mid][mid2]:
                l = mid2 + 1
            elif target < matrix[mid][mid2]:
                r = mid2 - 1
            elif target == matrix[mid][mid2]:
                return True
            else:
                break
        return False
        