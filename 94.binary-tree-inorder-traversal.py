#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        stack = []
        node = root
        
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                #左边遍历完
                node = node.left
            node = stack.pop()
            result.append(node.val) #取中间的
            node = node.right #取右边的

        return result
# @lc code=end

