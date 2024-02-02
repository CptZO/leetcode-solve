# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.


# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]


# Constraints:

# 10 <= low <= high <= 10^9

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        s = '123456789'
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s):
                num = int(s[i:j+1])

                if num > high:
                    break
                if low <= num:
                    res.append(num)
                j += 1
            i += 1
        return sorted(res)

# Link : https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02
