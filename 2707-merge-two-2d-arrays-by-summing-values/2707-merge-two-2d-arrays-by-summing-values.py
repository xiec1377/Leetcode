class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        myDict = {}
        res = []
        for key, val in nums1:
            if key in myDict:
                myDict[key] += val
            else:
                myDict[key] = val
            
        for key, val in nums2:
            if key in myDict:
                myDict[key] += val
            else:
                myDict[key] = val
        
        for key in myDict.keys():
            res.append([key, myDict[key]])
        return sorted(res, key=lambda x: x[0])

        