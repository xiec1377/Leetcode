class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # use djikstra's algo for shortest path
        visited = set()
        heap = []
        heapq.heappush(heap,[0,k])
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        while heap:
            wei,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return wei

            for nei,w in graph[node]:
                heapq.heappush(heap,[w+wei,nei])

        return -1
        


        