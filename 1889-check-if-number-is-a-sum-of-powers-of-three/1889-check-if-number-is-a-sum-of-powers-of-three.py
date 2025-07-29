class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # cannot have 2 in base 3
        if n == 0:
            return True
        if n % 3 == 2:
            return False
        return self.checkPowersOfThree(n // 3)
        # # log3 n until whole positive number reached, else false
        # res = math.log(n, 3)
        # print("res:", res)
        # if res.is_integer():
        #     print("here")
        #     return True
        # else:
        #     diff = n - (3 ** math.floor(res))
        #     print("diff:", diff)
        #     if diff < 0:
        #         return False
        #     return self.checkPowersOfThree(diff)

        