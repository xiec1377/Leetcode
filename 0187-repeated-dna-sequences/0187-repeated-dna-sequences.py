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
            print("s[i", s[i])
            j = i + 10
            if j <= len(s): 
                # print("s[j\]", s[j])
                k = s[i:j]
                print("k substring:", k)
                myMap[k] += 1
                if myMap[k] > 1 and k not in res:
                    print("here")
                    res.append(k)

        return res

        

