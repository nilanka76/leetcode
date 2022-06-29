# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Definition for a binary tree node.
# https://leetcode.com/problems/binary-tree-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root: return []
        temp = root
        queue = [temp]
        treeList = []
        while queue:
            qLen =len(queue)
            tempList = []
            for i in range(qLen):
                curr = queue.pop(0)
                tempList.append(curr.val)
                if curr.left:   queue.append(curr.left)
                if curr.right:  queue.append(curr.right)
            treeList.append(tempList)
        return treeList