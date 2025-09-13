class Solution:
    def doesAliceWin(self, s: str) -> bool:
        numVowels = 0
        vowels = set()
        vowels.update(['a', 'e', 'i', 'o', 'u'])
        for c in s:
            if c in vowels:
                numVowels += 1
        # if numVowels is even, Alice wins 
        # if numVowels is odd, Alice still wins
        return numVowels > 0