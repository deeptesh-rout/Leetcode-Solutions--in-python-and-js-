'''
You are given an array of strings names, and an array heights that consists of distinct positive integers.
Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:
n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
'''


class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Create a list of tuples where each tuple contains a name and its corresponding height.
        people = list(zip(names, heights))
        # Sort the list of tuples based on the heights in descending order.
        people.sort(key=lambda x: x[1], reverse=True)
        # Extract the sorted names from the list of tuples.
        sorted_names = [person[0] for person in people]

        return sorted_names


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
solution = Solution()
print(solution.sortPeople(names, heights))
