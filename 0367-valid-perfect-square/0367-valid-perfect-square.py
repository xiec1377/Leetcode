class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        j = num
        while i <= j:
            med = (i + j) // 2
            medSquare = med ** 2
            if medSquare == num:
                return True
            elif medSquare > num:
                j = med - 1
            elif medSquare < num:
                i = med + 1
        return False