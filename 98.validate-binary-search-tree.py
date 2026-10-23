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
        def dfs(node: TreeNode | None, min_limit, max_limit):
            if node is None:
                return True
            if node.val <= min_limit or node.val >= max_limit:
                return False

            left_is_BST = dfs(node.left, min_limit, node.val)
            right_is_BST = dfs(node.right, node.val, max_limit)

            return left_is_BST and right_is_BST
        return dfs(root, float("-inf"), float("inf"))
# @lc code=end

