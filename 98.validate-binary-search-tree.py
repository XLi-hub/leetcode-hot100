#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        pre = float("-inf")

        def inorder(node: TreeNode | None) -> bool:
            if node is None:
                return True

            nonlocal pre

            left_is_inorder = inorder(node.left)

            if node.val <= pre:
                return False
            pre = node.val

            right_is_inorder = inorder(node.right)

            return left_is_inorder and right_is_inorder
        return inorder(root)
# @lc code=end

