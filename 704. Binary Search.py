class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (left+right) //2
        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1

            mid = (left+right) // 2

        return -1