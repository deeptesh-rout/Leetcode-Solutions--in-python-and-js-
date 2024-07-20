'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        # if first number is not 0, zero is missing.
        if sorted_nums[0] != 0:
            return 0
        for i in range(length - 1):
            if sorted_nums[i+1] - sorted_nums[i] != 1:
                return sorted_nums[i] + 1
        # If no missing number is found, return a default value.
        return sorted_nums[-1] + 1


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))
