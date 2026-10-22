#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        for char in s:
            if char.isdigit(): #如果是数字
                current_num = current_num*10 + int(char)
            elif char == "[":
                stack.append(current_num)
                current_num = 0 #current_num置0
                stack.append("[")
            elif char == "]":
                sub_strs = []
                while stack[-1] != "[":
                    sub_strs.append(stack.pop())

                #反转sub_strs
                sub_strs.reverse()
                inner_str = "".join(sub_strs)

                #把"["pop出去
                stack.pop()

                #读取"["前面的数字并pop出去
                times = stack.pop()

                stack.append(inner_str*times)
            else: #如果是字母
                stack.append(char)

        return "".join(stack)

                    
# @lc code=end

