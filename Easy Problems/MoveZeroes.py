'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                length -= 1     # Decrease the length since we've moved an element to the end
            else:
                # Move to the next element in the list by incrementing the index i by 1 (i = i + 1).
                i += 1


nums = [0, 1, 0, 0, 1, 0]
solution = Solution()
print(solution.moveZeroes(nums))
