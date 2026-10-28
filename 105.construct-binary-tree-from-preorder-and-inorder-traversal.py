#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(root)

        root_left = self.buildTree(preorder[1:1+root_index],inorder[:root_index])
        root_right = self.buildTree(preorder[1+root_index:],inorder[root_index+1:])

        return root
    # @lc code=end

