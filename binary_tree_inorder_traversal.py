# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        # Recursive solution
        treeList = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            treeList.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return treeList

        # iterative solution
        treeList = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            treeList.append(curr.val)
            curr = curr.right
        return treeList