'''
Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

Example 1:
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Example 2:
Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

Example 3:
Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.

Constraints:

0 <= num <= 106
'''


class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num_str = str(num)
        # Reverse the string representation of the number and remove leading and trailing zeros.
        reversed_num = num_str[::-1].strip('0')
        # Get the lengths of the original number and its reverse.
        num_length = int(len(num_str))
        reversed_num_length = int(len(reversed_num))

        # Check if the lengths are equal.
        if num_length == reversed_num_length:
            return
        # Check if the original number is the same as its reverse.
        elif num_str == str(num_str[::-1]):
            return True
        else:
            return False


num = 1300
solution = Solution()
print(solution.isSameAfterReversals(num))
