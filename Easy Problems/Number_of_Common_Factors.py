'''
Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.

Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
 
Constraints:
1 <= a, b <= 1000
'''


class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a_factors = []
        for i in range(1, a + 1):
            divisor = i
            if a % divisor == 0:
                a_factors.append(divisor)

        b_factors = []
        for i in range(1, b + 1):
            divisor = i
            if b % divisor == 0:
                b_factors.append(divisor)

        common_factors = 0
        for i in range(len(a_factors)):
            for j in range(len(b_factors)):
                if a_factors[i] == b_factors[j]:
                    common_factors += 1

        return common_factors


a = 25
b = 30
solution = Solution()
print(solution.commonFactors(a, b))
