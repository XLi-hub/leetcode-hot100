#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * (n+1)
        for first, last, seats in bookings:
            diff[first-1] += seats
            diff[last] -= seats

        answer = [0] * n
        last_seats = 0
        for i in range(n):
            answer[i] = last_seats + diff[i]
            last_seats = answer[i]

        return answer
# @lc code=end

