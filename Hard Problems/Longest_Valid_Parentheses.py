'''
Given a string containing just the characters '(' and ')', 
return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = max_length = 0

        # Scan from left to right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right >= left:
                left = right = 0

        left = right = 0

        # Scan from right to left
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left >= right:
                left = right = 0

        return max_length


s = ")("
solution = Solution()
print(solution.longestValidParentheses(s))
