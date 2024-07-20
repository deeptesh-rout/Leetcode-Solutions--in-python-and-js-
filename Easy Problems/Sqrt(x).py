'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
Constraints:
0 <= x <= 231 - 1
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Special case for 0, as its square root is 0.
        if x == 0:
            return 0

        # Initialise guess to the given number.
        guess = x

        # Use Newton's method to approximate the square root.
        while guess * guess > x:
            guess = (guess + x // guess) // 2

        # Return the integer part of the square root.
        return guess


x = 8
solution = Solution()
print(solution.mySqrt(x))
