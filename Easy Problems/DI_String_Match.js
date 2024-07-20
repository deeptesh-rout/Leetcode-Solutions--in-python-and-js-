/*
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

Constraints:
1 <= s.length <= 105
s[i] is either 'I' or 'D'.
*/

/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function (s) {
    const length = s.length;
    let rangeNums = [];
    for (let i = 0; i <= length; i++) {
        rangeNums.push(i);
    }
    let output = [];
    for (let char of s) {
        if (char == "D") {
            output.push(rangeNums.pop());
        }
        else if (char == "I") {
            output.push(rangeNums.shift());
        }
    }
    output.push(rangeNums.pop());
    return output;
};

let s = "IDID";
console.log(diStringMatch(s));