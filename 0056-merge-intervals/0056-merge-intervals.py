class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            last_end = merged[-1][1]
            if last_end >= start:
                new_end = max(last_end, end)
                merged[-1][1] = new_end
            else:
                merged.append([start, end])
        return merged