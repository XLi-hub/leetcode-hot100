#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: list[int]):
        #前缀和
        self.prefix_num = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.prefix_num[i+1] = self.prefix_num[i] + nums[i]

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_num[right+1] - self.prefix_num[left]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

