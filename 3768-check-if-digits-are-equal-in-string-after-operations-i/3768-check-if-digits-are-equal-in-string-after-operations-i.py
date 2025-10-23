class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2 and (s[0] == s[1]):
            return True
        while len(s) > 2:
            newStr = ""
            for i in range(1, len(s)):
                sum = (int(s[i-1])+int(s[i])) % 10
                newStr += str(sum)
            s = newStr
        if s[0] == s[1]:
            return True
        else:
            return False        