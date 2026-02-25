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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = self.findNode(root, key)
        return root
    def findSuccessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = root.right
        while root is not None and root.left is not None:
            root = root.left
        return root
    def findNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.val > key:
            root.left = self.findNode(root.left, key)
        elif root.val < key:
            root.right = self.findNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            suc = self.findSuccessor(root)
            root.val = suc.val
            root.right = self.findNode(root.right, suc.val)
        return root

        
        
        


