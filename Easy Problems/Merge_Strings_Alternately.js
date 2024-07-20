/*
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
*/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
    let mergedWords = "";
    let lenWord1 = word1.length;
    let lenWord2 = word2.length;
    let length = lenWord1 + lenWord2;
    for (let i = 0; i < length; i++) {
        if (i % 2 == 0) {
            mergedWords += word1[0];
            word1 = word1.slice(1);
        } else {
            mergedWords += word2[0];
            word2 = word2.slice(1);
        }
        if (word1.length == 0) {
            mergedWords += word2;
            break;
        }
        if (word2.length == 0) {
            mergedWords += word1;
            break;
        }
    }
    return mergedWords;
};

let word1 = "abcd";
let word2 = "pq";
console.log(mergeAlternately(word1, word2));