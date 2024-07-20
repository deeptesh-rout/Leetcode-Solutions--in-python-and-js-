'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect_nums = []
        num_count = {}
        for num in nums1:
            num_count[num] = num_count.get(num, 0) + 1
        for num in nums2:
            if num in num_count and num_count[num] > 0:
                intersect_nums.append(num)
                num_count[num] = num_count[num] - 1

        return intersect_nums


nums1 = [1, 2, 2, 1]
nums2 = [2]
solution = Solution()
print(solution.intersect(nums1, nums2))


class Solution(object):
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_length = len(nums1)
        nums2_length = len(nums2)

        if nums1_length < nums2_length:
            shorter_arr = nums1
            longer_arr = nums2
        else:
            shorter_arr = nums2
            longer_arr = nums1

        result = []
        used_indices = set()

        for num1 in shorter_arr:
            for i, num2 in enumerate(longer_arr):
                if num2 == num1 and i not in used_indices:
                    result.append(num1)
                    used_indices.add(i)
                    break

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()
print(solution.intersect1(nums1, nums2))
