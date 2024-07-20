'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        # If the length of the string is odd, it cannot be balanced.
        if length % 2 != 0:
            return False
        else:
            # Initialise an empty stack to keep track of opening parentheses.
            stack = []
            for char in s:
                # If the character is an opening parenthesis, push it onto the stack.
                if char == '(' or char == '[' or char == '{':
                    stack.append(char)
                # If the character is a closing parenthesis.
                elif char == ')' and stack and stack[-1] == '(':
                    # If there's a matching opening parenthesis on the stack, pop it.
                    stack.pop()
                elif char == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack and stack[-1] == '{':
                    stack.pop()
                # If none of the above conditions are met, the parentheses are not balanced.
                else:
                    return False
            # If the stack is empty, all parentheses are matched.
            return len(stack) == 0


s = "{()[]}"
solution = Solution()
print(solution.isValid(s))
