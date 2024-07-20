'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        length = len(nums)
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key, value in count.items():
            if value > (length / 2):
                return key


nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
print(solution.majorityElement(nums))
