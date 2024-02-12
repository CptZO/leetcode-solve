# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


# Code
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        k = max(hmap, key=lambda x: hmap[x])
        return k

    # link:https://leetcode.com/problems/majority-element/?envType=daily-question&envId=2024-02-12
