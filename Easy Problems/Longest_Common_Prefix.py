'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest_word = min(strs, key=len)

        for i, char in enumerate(shortest_word):
            for word in strs:
                if word[i] != char:
                    return shortest_word[:i]

        return shortest_word


strs = ["flower", "flow", "flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
