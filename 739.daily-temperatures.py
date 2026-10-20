#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        answer = n*[0]
        for i in range(n):
            cur_temp = temperatures[i]
            while stack and cur_temp > temperatures[stack[-1]]:
                pre_index = stack.pop()
                answer[pre_index] = i-pre_index
            stack.append(i)
        return answer

# @lc code=end

