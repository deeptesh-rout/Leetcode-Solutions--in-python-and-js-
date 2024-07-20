/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
*/

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    if (strs == null || strs.length == 0) {
        return "";
    }
    let shortestWord = strs[0];
    for (let word of strs) {
        if (word.length < shortestWord.length) {
            shortestWord = word;
        }
    }
    for (let i = 0; i < shortestWord.length; i++) {
        for (let word of strs) {
            if (word[i] != shortestWord[i]) {
                return shortestWord.slice(0, i);
            }
        }
    }
    return shortestWord;
};

let strs = ["flower", "flow", "flight"];
console.log(longestCommonPrefix(strs));