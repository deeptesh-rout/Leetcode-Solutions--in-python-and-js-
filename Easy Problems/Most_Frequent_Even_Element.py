'''
Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
'''


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num % 2 == 0:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
        if not count:  # If there are no even elements.
            return -1

        max_value = max(count.values())
        most_frequent_even = []
        for key, value in count.items():
            if value == max_value:
                most_frequent_even.append(key)

        return min(most_frequent_even)


nums = [4, 4, 4, 9, 2, 4]
solution = Solution()
print(solution.mostFrequentEven(nums))
