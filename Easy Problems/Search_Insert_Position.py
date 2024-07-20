'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i, num in enumerate(nums):
            # If the current number is greater than the target value, then the target value should be inserted at this (current number) position.
            # If the current number is equal to the target value, then report the current value position.
            if num >= target:
                return i
        # If the target value is greater than all numbers in the list, it belongs at the end of the list, so return the length of the list.
        return len(nums)


nums = [1, 3, 5, 6]
target = 2
solution = Solution()
print(solution.searchInsert(nums, target))
