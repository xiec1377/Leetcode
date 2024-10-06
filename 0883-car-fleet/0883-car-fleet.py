class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        arr = []
        stack = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr.sort()
        for i in range(len(arr) - 1, -1, -1):
            stack.append(arr[i])
            if len(stack) >= 2:
                timeToDest = (target - stack[-1][0]) / float(stack[-1][1])
                topTime = (target - stack[-2][0]) / float(stack[-2][1])
                if topTime >= timeToDest:
                    stack.pop()
        return len(stack)
        