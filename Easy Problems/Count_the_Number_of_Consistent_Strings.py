'''
You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 
Constraints:
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
'''


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        for word in words[:]:
            for char in word:
                if char not in allowed:
                    words.remove(word)
                    break

        return len(words)


allowed = "fstqyienx"
words = ["n", "eeitfns", "eqqqsfs", "i", "feniqis",
         "lhoa", "yqyitei", "sqtn", "kug", "z", "neqqis"]
solution = Solution()
print(solution.countConsistentStrings(allowed, words))


# SECOND SOLUTION:

'''
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_words = []
        for word in words:
            is_allowed = True
            for char in word:
                if char not in allowed:
                    words.remove(word)
            if is_allowed == True:
                allowed_words.append(word)

        return len(allowed_words)
'''
