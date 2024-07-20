'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sorted_nums = sorted(
            map(str, nums), key=lambda x: x * 100, reverse=True)
        result = "".join(sorted_nums).lstrip("0") or "0"
        return result


nums = [3, 30, 34, 5, 9]
solution = Solution()
print(solution.largestNumber(nums))
