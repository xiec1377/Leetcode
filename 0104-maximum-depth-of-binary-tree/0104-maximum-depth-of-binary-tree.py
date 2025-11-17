# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque()
        q.append((root, 1))
        maxD = float('-inf')
        while q:
            node, depth = q.popleft()
            if node == None:
                return 0
            maxD = max(maxD, depth)
            if node.left != None:
                q.append((node.left, depth + 1))
            if node.right != None:
                q.append((node.right, depth + 1))
        return maxD
            

