class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        isVowel = False
        isConsonant = False
        for char in word.lower():
            if not ((char >= '0' and char <= '9') or (char >= 'a' and  char <= 'z')):
                return False
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                isVowel = True
            elif not (char >= '0' and char <= '9'):
                isConsonant = True
        return isVowel and isConsonant

        