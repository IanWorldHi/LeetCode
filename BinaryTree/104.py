from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.dfs(root.left), self.dfs(root.right))
    def bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            depth = 0
            qu = deque([root])
            while qu:
                size = len(qu)
                depth +=1
                for i in range(size):
                    popped = qu.popleft()
                    if popped.left:
                        qu.append(popped.left)
                    if popped.right:
                        qu.append(popped.right)
        return depth



        