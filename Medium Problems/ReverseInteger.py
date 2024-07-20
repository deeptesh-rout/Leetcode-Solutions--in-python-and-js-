'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = str(x)
        output = 0
        if num[0] == "-":
            reversed_num = "-" + num[:0:-1]
            output = int(reversed_num)
        else:
            reversed_num = num[::-1]
            output = int(reversed_num)

        if output < -2**31 or output > 2**31 - 1:
            return 0
        else:
            return output


x = -123
solution = Solution()
print(solution.reverse(x))
