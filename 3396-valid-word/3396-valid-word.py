class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        isVowel = False
        isConsonant = False
        for char in word.lower():
            if (char >= '0' and char <= '9') or (char >= 'a' and  char <= 'z'):
                print("valid char")
            else:
                print("invalid char")
                return False
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                print("vowel")
                isVowel = True
            elif not (char >= '0' and char <= '9'):
                print("consonant")
                isConsonant = True
        return isVowel and isConsonant

        