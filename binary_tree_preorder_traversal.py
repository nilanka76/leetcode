# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        # Recursive solution
        treeList = []
        def preOrder(root):
            if not root: #root == None
                return
            treeList.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return treeList

        # iterative solution
        if not root: return [] 
        treeItems = []
        stack = [root]   
        while stack:
            curr = stack.pop()
            treeItems.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)         
        return treeItems
        