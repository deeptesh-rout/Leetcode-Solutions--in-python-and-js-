'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''


class Solution(object):
    def mergeAlternately1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        words = ""

        for i in range(len(word1) + len(word2)):
            if i % 2 == 0:
                words += word1[0]
                word1 = word1[1::]
            else:
                words += word2[0]
                word2 = word2[1::]

            if len(word1) == 0:
                words += word2
                break

            if len(word2) == 0:
                words += word1
                break

        return words

    def mergeAlternately2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        words = ""
        count1 = 0
        count2 = 0
        for i in range(len(word1) + len(word2)):

            if len(word1) <= count1:
                words += word2[count2::]
                break

            if len(word2) <= count2:
                words += word1[count1::]
                break

            if i % 2 == 0:
                words += word1[count1]
                count1 += 1
            else:
                words += word2[count2]
                count2 += 1

        return words


word1 = "abcd"
word2 = "pq"
solution = Solution()
print(solution.mergeAlternately1(word1, word2))
print(solution.mergeAlternately2(word1, word2))
