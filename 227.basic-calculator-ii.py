#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        pre_sign = "+"
        n = len(s)
        for i in range(n):
            char = s[i]
            if char.isdigit():
                num = num*10 + int(char)
            if not char.isdigit() or i == n-1:
                if pre_sign == "+":
                    stack.append(num)
                elif pre_sign == "-":
                    stack.append(-num)
                elif pre_sign == "*":
                    top = stack.pop()
                    plus = top*num
                    stack.append(plus)
                elif pre_sign == "/":
                    top = stack.pop()
                    plus = int(top/num)
                    stack.append(plus)

                pre_sign = char
                num = 0
        return sum(stack)
# @lc code=end

