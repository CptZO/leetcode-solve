# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1


# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


# code

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1


# link : https://leetcode.com/problems/first-unique-character-in-a-string/?envType=daily-question&envId=2024-02-05
