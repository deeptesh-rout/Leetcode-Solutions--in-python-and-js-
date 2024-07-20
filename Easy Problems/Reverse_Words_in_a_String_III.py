'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace 
and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
 
Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reversed_s = ""
        for word in words:
            reversed_word = word[::-1]
            reversed_s += reversed_word + " "
        return reversed_s.strip()


s = "Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(s))
