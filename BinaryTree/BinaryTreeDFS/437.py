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
        self.dfs(root, targetSum)
        return self.count
    def dfs2(self, root: Optional[TreeNode], targetSum: int):
        return
    def dfs(self,  root: Optional[TreeNode], targetSum: int):
        if not root:
            return 
        self.test(root, targetSum)
        if root.right:
            self.dfs(root.right, targetSum)
        if root.left:
            self.dfs(root.left, targetSum)
    def test(self, root: Optional[TreeNode], targetSum: int):
        if not root:
            return 
        targetSum -= root.val
        if targetSum == 0:
            self.count += 1
        if root.right:
            self.test(root.right, targetSum)
        if root.left:
            self.test(root.left, targetSum)
    
        




