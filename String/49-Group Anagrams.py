# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


# Code
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = collections.defaultdict(list)

        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1   # ASCII value of "C" varible ( 81- 80 )
        #     res[tuple(count)].append(s)
        # return res.values()

        setHash = defaultdict(list)
        for i in strs:
            setHash[tuple(sorted(i))].append(i)
        return list(setHash.values())

    # link: https://leetcode.com/problems/group-anagrams/?envType=daily-question&envId=2024-02-06
