# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

# Code:

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)-1, -1, -1):
            currtemp = temperatures[i]

            while stk and currtemp >= temperatures[stk[-1]]:
                stk.pop()

            if stk:
                res[i] = stk[-1]-i

            stk.append(i)

        return res

# link : https://leetcode.com/problems/daily-temperatures/description/?envType=daily-question&envId=2024-01-31
