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
        heapq.heappush(heap, [0, k])
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        print("graph:", graph)

        while heap:
            print("in heap")
            weight, u = heapq.heappop(heap)
            print(u, weight)
            if u in visited:
                continue
            visited.add(u)
            if len(visited) == n:
                return weight
            for v, w in graph[u]:
                print("v, w:", v, w)
                heapq.heappush(heap, [w+weight, v])

        return -1
        


        