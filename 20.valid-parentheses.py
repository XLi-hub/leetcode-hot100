#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in {"(","[","{"}:
                stack.append(char)

            else:
                if not stack:
                    return False

                top_ele = stack.pop()
                if mapping[char] != top_ele:
                    return False

        if stack:
            return False
        else:
            return True
# @lc code=end
         
