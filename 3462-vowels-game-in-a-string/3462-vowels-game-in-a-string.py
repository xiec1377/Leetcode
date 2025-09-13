class Solution:
    def doesAliceWin(self, s: str) -> bool:
        numVowels = 0
        vowels = set()
        vowels.update(['a', 'e', 'i', 'o', 'u'])
        for c in s:
            if c in vowels:
                numVowels += 1
        # return numVowels % 2 != 0 or numVowels % 2 == 0 and numVowels > 0   
        return numVowels > 0