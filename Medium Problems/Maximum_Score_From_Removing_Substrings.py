'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 
Constraints:
1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
'''


class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pairs(s, first, second, score):
            stack = []
            count = 0

            for char in s:
                if char == second and stack and stack[-1] == first:
                    stack.pop()
                    count += score
                else:
                    stack.append(char)

            return "".join(stack), count

        # Ensure we handle the higher score pair first
        if x > y:
            s, count_larger = remove_pairs(s, 'a', 'b', x)
            s, count_smaller = remove_pairs(s, 'b', 'a', y)
        else:
            s, count_smaller = remove_pairs(s, 'b', 'a', y)
            s, count_larger = remove_pairs(s, 'a', 'b', x)

        return count_larger + count_smaller


s = "aabbaaxybbaabb"
x = 5
y = 4
solution = Solution()
print(solution.maximumGain(s, x, y))
