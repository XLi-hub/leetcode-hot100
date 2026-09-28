class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        slow = 0
        fast = 0
        sum = 0
        min_len = float("inf")
        while fast < len(nums):
            sum += nums[fast]
            while sum >= target:
                min_len = min(min_len,fast-slow+1)
                sum -= nums[slow]
                slow += 1

            fast += 1

        return min_len if min_len != float("inf") else 0 
            
