from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.dfs(root, targetSum, [])
        return self.count
    def dfs(self,  root: Optional[TreeNode], targetSum: int, path: list):
        if not root:
            return False
        path.append(root.val)
        if sum(path) == targetSum:
            self.count+=1
            path.pop(0)
        elif sum(path) > targetSum:
            path.pop(0)
        if root.left:
            self.dfs(root.left, targetSum, path)
        if root.right:
            self.dfs(root.right, targetSum, path)
        
    
        




