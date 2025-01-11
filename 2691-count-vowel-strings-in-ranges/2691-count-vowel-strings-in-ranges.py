class Solution(object):
    def isVowel(self, char):
        return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
    def startAndEndWithVowels(self, word):
        print("word last:", word[-1:])
        return self.isVowel(word[0]) and self.isVowel(word[-1:]) 
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # create array of length of words to store number of words that start and end with vowels
        arr = [0] * len(words)
        total = 0
        ans = [0] * len(queries)
        for i, word in enumerate(words):
            print("i:", i, "word:", word)
            if self.startAndEndWithVowels(word):
                print("correct case")
                total += 1
            arr[i] = total
        print("arr:", arr)

        for i, query in enumerate(queries):
            print("query:", query)
            if query[0] == 0:
                diff = 0
            else:
                diff = arr[query[0] - 1]
            print("diff:", diff)
            ans[i] = arr[query[1]] - diff
        return ans
