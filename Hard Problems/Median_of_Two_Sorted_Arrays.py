'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).


Example 1:

Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1, 2, 3] and median is 2.
Example 2:

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.50000
Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two arrays.
        merged_nums = nums1 + nums2
        # Sort the merged array.
        sorted_nums = sorted(merged_nums)
        # Get the length of the merged array.
        length = len(sorted_nums)

        # Handle the case where the merged array is empty.
        if length == 0:
            return 0.0
        # Handle the case where the merged array has even length.
        elif length % 2 == 0:
            index = length // 2
            # Calculate the average of the two middle elements.
            return (sorted_nums[index] + sorted_nums[index - 1]) / 2.0
        # Handle the case where the merged array has odd length.
        else:
            index = length // 2
            # Return the middle element directly.
            return float(sorted_nums[index])


nums1 = [1, 2]
nums2 = [3, 4]
solution = Solution()
median = solution.findMedianSortedArrays(nums1, nums2)
print(median)
