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

        def f(node: TreeNode | None):
            if node is None:
                return 

            #中序遍历
            #左
            f(node.left)
            #中
            result.append(node.val)
            #右
            f(node.right)

        f(root)
        return result
# @lc code=end

