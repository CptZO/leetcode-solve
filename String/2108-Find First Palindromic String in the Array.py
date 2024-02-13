# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.


# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# Example 2:

# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# Example 3:

# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.

# code

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def palindromeOrNot(s):
            p1, p2 = 0, len(s)-1
            while p1 < p2:
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1
                else:
                    return False
            return True

        for i in range(len(words)):
            if palindromeOrNot(words[i]) == True:
                return words[i]

        return ""

    # link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/?envType=daily-question&envId=2024-02-10
