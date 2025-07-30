class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        numPaths = 0
        pq = []
        heapq.heappush(pq, [0, 0])
        visited = []
        roadsDict = {}
        times = []
        minPaths = [0] * n
        minPaths[0] = 1
        minTime = [float('inf')] * n
        minTime[0] = 0
        MOD = 10 ** 9 + 7
        if not roads:
            return n
        for source, dest, time in roads:
            if source in roadsDict.keys():
                roadsDict[source].append([dest, time])
            else:
                roadsDict[source] = [[dest, time]]
            if dest in roadsDict.keys():
                roadsDict[dest].append([source, time])
            else:
                roadsDict[dest] = [[source, time]]
        # for source in roadsDict.keys():
        #     for dest, time in roadsDict[source]:
        #         print(source, ", ", dest, ", ", time)

        while pq:
            totalTime, node  = heapq.heappop(pq)
            if totalTime > minTime[node]:
                continue
            if not node in visited:
                visited.append(node)
                for dest, time in roadsDict[node]:
                    print(dest, time)
                    newTime = totalTime + time
                    if newTime < minTime[dest]:
                        minTime[dest] = newTime
                        minPaths[dest] = minPaths[node]
                        heapq.heappush(pq, [newTime, dest])
                    elif newTime == minTime[dest]:
                        minPaths[dest] += minPaths[node]
        return minPaths[n-1] % MOD




        