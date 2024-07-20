'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''


class Solution(object):
    def singleNumber1(self, nums):
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
            if count.get(num) == 1:
                return num


nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber1(nums))


class Solution(object):
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber2(nums))
