from typing import Optional
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.bfs(root, 0, [])
    def bfs(self, root: Optional[TreeNode], level: int, result: List[List[int]]) -> List[int]:
        if root is None:
            return []
        depth = 0
        qu = deque([root])
        while qu:
            size = len(qu)
            depth +=1
            result.append([])
            for i in range(size):
                popped = qu.popleft()
                result[depth-1].append(popped.val)
                if popped.left:
                    qu.append(popped.left)
                if popped.right:
                    qu.append(popped.right)
        result2 = []
        for i in result:
            result2.append(i[-1])
        return result2
        
        
        
        