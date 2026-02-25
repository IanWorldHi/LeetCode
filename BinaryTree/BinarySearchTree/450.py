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
        node = self.findNode(root, key)
        self.fixNode(node)
        return root
    def findNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            return root
        elif root.val > key:
            return self.findNode(root.left, key)
        else:
            return self.findNode(root.right, key)
    def findSuccessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = root.right
        while root is not None and root.left is not None:
            root = root.left
        return root
    def fixNode(self, root: Optional[TreeNode]):
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return None
        elif root.left and not root.right:
            root = root.left
        elif root.right and not root.left:
            root = root.right
        else:
            suc = self.findSuccessor(root)
            root.val = suc.val
            root.right = self.fixNode(root.right)        
        
        
        


