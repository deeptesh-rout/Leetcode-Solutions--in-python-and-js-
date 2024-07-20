'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 
Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''


# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sentence = len(s.lower())
#         for i in range(sentence):
#             if sentence.count(sentence[i]) == 1:
#                 return i
#         return -1


# s = "LeetCode"
# char_index = Solution().firstUniqChar(s)
# print(char_index)


# Below is the optimised code to avoid "Time Limit Exceeded" errors:

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to store the count of each character.
        char_count = {}

        # Count the frequency of each character in the string.
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find the index of the first unique character.
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no unique character is found, return -1.
        return -1


s = "LeetCode"
solution = Solution()
char_index = solution.firstUniqChar(s)
print(char_index)
