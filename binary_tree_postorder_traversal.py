# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root) -> list[int]:
        # Recursive solution
        treeList = []
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)  
            postOrder(root.right)
            treeList.append(root.val)
        postOrder(root)
        return treeList

        # iterative solution
        # if not root: return []
        # treeList= []
        # stack = [root]
        
        # while stack:
        #     curr = stack.pop()
        #     treeList.append(curr.val)
        #     if curr.left:
        #         stack.append(curr.left)
        #     if curr.right:
        #         stack.append(curr.right)
                
        # return treeList[ : : -1]
        