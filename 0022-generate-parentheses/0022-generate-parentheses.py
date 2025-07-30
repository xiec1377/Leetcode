class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        queue = deque()
        queue.append(("(", 1, 0))  # (current string, numOpen, numClosed)

        while queue:
            paren, numOpen, numClosed = queue.popleft()
            if numOpen == n and numClosed == n:
                res.append(paren)
                continue
            if numOpen < n:
                queue.append((paren + "(", numOpen + 1, numClosed))
            if numClosed < numOpen:
                queue.append((paren + ")", numOpen, numClosed + 1))
        return res