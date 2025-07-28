class Solution:
    def makeFancyString(self, s: str) -> str:
        firstChar = ''
        countChar = 0
        res = ""
        for i in range(len(s)):
            if s[i] == firstChar:
                countChar += 1
                if countChar >= 3:
                    continue

            else:
                firstChar = s[i]
                countChar = 1
            res += s[i]
        return res
        