#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []

        def f(node: TreeNode | None):
            if node is None:
                return

            #后序遍历
            #左
            f(node.left)
            #右
            f(node.right)
            #中
            result.append(node.val)

        f(root)
        return result
# @lc code=end

