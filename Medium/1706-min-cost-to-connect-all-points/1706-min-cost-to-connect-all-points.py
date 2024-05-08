class Solution(object):
    def getManhattanDistance(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #use kruskal's algo

        # if len(points) == 1:
        #     return 0
        # graph = defaultdict(list)
        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         distance = self.getManhattanDistance(points[i][0], points[i][1], points[j][0], points[j][1])
        #         graph[i].append([distance, j])
        #         graph[j].append([distance, i])
        # print("graph:", graph)
        # visited = [0] * len(points)
        # visited[0] = 1
        # heap = graph[0]
        # heapq.heapify(heap)
        # # print("heap:", heap)
        # ans = 0
        # cnt = 1

        # while heap:
        #     dis, pt = heapq.heappop(heap)
        #     print("dis:", dis)
        #     print("pt:", pt)
        #     if not visited[pt]:
        #         visited[pt] = 1
        #         ans += dis
        #         cnt += 1
        #         # if len(visited) > len(points):
        #         #     break
        #         for d, v in graph[pt]:
        #             heapq.heappush(heap, [d, v])
        #     if cnt >= len(points): break
        # return ans
               
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = self.getManhattanDistance(points[i][0], points[i][1], points[j][0], points[j][1])
                graph[i].append([d, j])
                graph[j].append([d, i])
        count = 1
        ans = 0
        visited = set()
        visited.add(0)
        heap = graph[0]
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if len(visited) == len(points):
                break
            if j not in visited:
                visited.add(j)
                count += 1
                ans += d
                for node in graph[j]: heapq.heappush(heap, node)
            # if count >= len(points): break        
        return ans
        