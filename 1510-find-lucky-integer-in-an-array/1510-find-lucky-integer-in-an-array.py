class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxLucky = float('-inf')
        myDict = {}
        for num in arr:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        for key in myDict.keys():
            if myDict[key] == key:
                maxLucky = max(maxLucky, myDict[key])
        if maxLucky != float('-inf'):
            return maxLucky
        else:
            return -1







        # maxLucky = float('-inf')
        # firstNum = float('-inf')
        # freq = 0
        # for i in range(len(arr)):
        #     if arr[i] == firstNum:
        #         freq += 1
        #         if freq == firstNum and i == len(arr) - 1:
        #             maxLucky = max(freq, maxLucky)
        #     else:
        #         if freq == firstNum:
        #             maxLucky = max(freq, maxLucky)
        #         freq = 1
        #         firstNum = arr[i] 
        # if maxLucky == float('-inf'):
        #     return -1
        # else:
        #     maxLucky = max(freq, maxLucky)
        #     return maxLucky

        