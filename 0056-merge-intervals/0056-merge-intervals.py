class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort by start 
        intervals.sort(key=lambda interval: interval[0])
        result = []
        result.append(intervals[0])
        for start, end in intervals:
            prev_start, prev_end = result[-1][0], result[-1][1]
            # print("start:", start, "end:", end)
            # print("prev_end", prev_end)
            if start <= prev_end and start >= prev_start:
                # print("in case")
                print([prev_start, max(end, prev_end)])
                result.pop() 
                result.append([prev_start, max(end, prev_end)])
            else:
                # print("in else")
                print([start, end])
                result.append([start, end])
            
            # print("result:", result)
        return result