class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = ""
        if numerator == 0:
            return "0"
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        quotient = numerator // denominator
        remainder = numerator % denominator
        result += str(quotient)
        if remainder == 0:
            return result
        result += "."
        print("result after . :", result)
        # handler repeating remainder
        remainderMap = {} # key is remainder, value is index
        while remainder != 0:
            if remainder in remainderMap:
                idx = remainderMap[remainder]
                result = result[:idx] + "(" + result[idx:] + ")"
                break
            else:
                remainderMap[remainder] = len(result)
                remainder *= 10 # 0.7878.. => 7.8787....
                result += str(remainder // denominator)
                remainder %= denominator
        return result 

