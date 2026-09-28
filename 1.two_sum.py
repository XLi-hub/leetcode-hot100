class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i, x in enumerate(nums):
            y = target - x 
            if y in mp:
                return [i,mp[y]]
            else:
                mp[x] = i
        