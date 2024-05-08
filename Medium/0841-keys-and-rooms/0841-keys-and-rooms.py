class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for room in range(len(rooms)):
            for key in rooms[room]:
                # print("room:", room)
                # print("key:", key)
                graph[room].append(key)

        stack = []
        stack.append(0)
        unlocked = set()
        unlocked.add(0)

        while stack:
            room = stack.pop()
            # print("room popped:", room)
            for key in graph[room]:
                # print("key popped:", key)
                if key not in unlocked:
                    unlocked.add(key)
                    stack.append(key)
                if len(unlocked) == len(rooms):
                    return True

        return False