'''
You are given a positive integer num consisting of exactly four digits. 
Split num into two new integers new1 and new2 by using the digits found in num. 
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. 
Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

Example 1:
Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.

Example 2:
Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
 
Constraints:
1000 <= num <= 9999
'''


class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)

        splitted_num = list(num_str)

        min_digit1 = min(splitted_num)
        splitted_num.remove(min_digit1)

        min_digit2 = min(splitted_num)
        splitted_num.remove(min_digit2)

        max_digit1 = max(splitted_num)
        splitted_num.remove(max_digit1)

        max_digit2 = max(splitted_num)
        splitted_num.remove(max_digit2)

        num1 = int(min_digit1 + max_digit1)
        num2 = int(min_digit2 + max_digit2)

        result = num1 + num2

        return result


num = 2932
solution = Solution()
print(solution.minimumSum(num))
