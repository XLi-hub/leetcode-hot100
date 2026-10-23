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
        if not root:
            return []

        result = []
        stack = [root]
        while stack:
            node = stack.pop()

            #如果是整数，说明该记录了
            if isinstance(node,int):
                result.append(node)
                continue
            if node.right:
                stack.append(node.right)
            stack.append(node.val)
            if node.left:
                stack.append(node.left)
        return result
# @lc code=end

