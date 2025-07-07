class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort intervals by start time
        sortedEvents = sorted(events, key=lambda item: item[0])

        # use min-heap to sort events by end time
        minHeap = []
        result = 0

        i = 0
        n = len(events)
        lastDay = max(j for _, j in sortedEvents)

        for day in range(1, lastDay + 1):
            while i < n and sortedEvents[i][0] == day:
                heapq.heappush(minHeap, sortedEvents[i][1])
                i += 1
            
            # pop all events that passed
            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)
            
            # attend event that ends the earliest
            if minHeap:
                heapq.heappop(minHeap)
                result += 1

            if i == n and not minHeap: # if no event to attend
                break
        return result




       
        