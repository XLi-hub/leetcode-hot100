#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def f(node: Optional[TreeNode]):
            if node is None:
                return 
            #前序遍历
            #中
            result.append(node.val)
            #左
            f(node.left)
            #右
            f(node.right)

        f(root)
        return result
# @lc code=end

