class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return True
        if n % 3 == 2:
            return False
        return self.checkPowersOfThree(n // 3)