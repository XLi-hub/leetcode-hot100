#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        left_maxdepth = self.maxDepth(root.left)
        right_maxdepth = self.maxDepth(root.right)

        return max(left_maxdepth,right_maxdepth)+1
# @lc code=end

