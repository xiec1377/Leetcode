class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        k = ""
        myMap = defaultdict(int)
        res = []
        for i in range(len(s)-9):
            j = i + 10
            if j <= len(s): 
                k = s[i:j]
                myMap[k] += 1
                if myMap[k] > 1 and k not in res:
                    res.append(k)

        return res

        

