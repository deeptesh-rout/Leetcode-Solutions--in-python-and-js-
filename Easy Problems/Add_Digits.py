'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
 
Constraints:
0 <= num <= 231 - 1
'''


class Solution(object):
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        # First iteration to sum the digits of num.
        result1 = 0
        for digit in str(num):
            result1 += int(digit)

        # Second iteration to sum the digits of result1.
        result2 = 0
        for digit in str(result1):
            result2 += int(digit)

        # If result2 is a single digit, return it.
        if result2 <= 9:
            return result2

        # Else, return the sum of the digits of result2.
        else:
            x = 0
            for digit in str(result2):
                x += int(digit)
            return x


num = 199
solution = Solution()
print(solution.addDigits1(num))


class Solution(object):
    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num

        if num % 9 == 0:
            return 9

        return num % 9


num = 199
solution = Solution()
print(solution.addDigits2(num))
