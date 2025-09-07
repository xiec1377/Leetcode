class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        num_pairs = n // 2
        if n % 2 == 1:
            result.append(0)
        for i in range(1, num_pairs + 1):
            result.append(i)
            result.append(-i)
        return result