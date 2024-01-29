# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.


# Example 1:


# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:


# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12


# Constraints:

# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n


# Code

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def f(i, j, moveLeft):
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if moveLeft == 0:
                return 0
            ans = 0
            for a, b in moves:
                ans = (ans+f(i+a, j+b, moveLeft-1)) % (10**9+7)
            return ans
        return f(startRow, startColumn, maxMove)

    # Link : https://leetcode.com/problems/out-of-boundary-paths/?envType=daily-question&envId=2024-01-26
