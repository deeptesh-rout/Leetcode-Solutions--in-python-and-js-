/*
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 
Constraints:
1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
*/

/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
    let stack = [];

    for (let char of s) {
        if (char == ")") {
            let tempList = [];
            while (stack.length && stack[stack.length - 1] != "(") {
                tempList.push(stack.pop());
            }
            stack.pop();
            stack.push(...tempList);

        } else {
            stack.push(char);
        }
    }
    return stack.join("");
};

let s = "(ed(et(oc))el)";
console.log(reverseParentheses(s));