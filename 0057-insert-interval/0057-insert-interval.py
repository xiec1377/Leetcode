class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        result = []
        newStart = newInterval[0]
        newEnd = newInterval[1]
        while i < n and intervals[i][1] < newStart: # no overlap
            result.append(intervals[i])
            i += 1
        while i < n and newEnd >= intervals[i][0]: # new end is between existing interval
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        
        result.append([newStart, newEnd])
        while i < n: # rest of intervals after merging
            result.append(intervals[i])
            i += 1
        return result


        
            
            
        