#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return False,False,None

            left_has_p , left_has_q , left_x = dfs(node.left)
            right_has_p , right_has_q , right_x = dfs(node.right)

            current_has_p = left_has_p or right_has_p or node == p
            current_has_q = left_has_q or right_has_q or node == q

            current_x = None
            if left_x:
                current_x = left_x
            elif right_x:
                current_x = right_x
            elif current_has_p and current_has_q:
                current_x = node
            return current_has_p, current_has_q, current_x
        _,_,x = dfs(root)
        return x
# @lc code=end

