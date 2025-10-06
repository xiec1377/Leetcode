class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for num in arr:
            if num % 2 != 0: # odd
                oddCount += 1
                if oddCount == 3:
                    return True
            else:
                oddCount = 0
        return False

        