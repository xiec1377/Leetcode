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
               


        # manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = self.getManhattanDistance(points[i][0], points[i][1], points[j][0], points[j][1])
                graph[i].append([d, j])
                graph[j].append([d, i])
        cnt, ans, visited, heap = 1, 0, [0] * len(points), graph[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in graph[j]: heapq.heappush(heap, record)
            if cnt >= len(points): break        
        return ans
        