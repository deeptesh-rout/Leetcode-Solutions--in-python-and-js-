'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in nums:
            if count.get(num) >= 2:
                return num


nums = [3, 1, 3, 4, 2]
solution = Solution()
print(solution.findDuplicate(nums))


# SOLUTION NUMBER 2 :

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if i != j and nums[i] == nums[j]:
                    return nums[i]


nums = [3, 1, 3, 4, 2]
solution = Solution()
print(solution.findDuplicate(nums))
