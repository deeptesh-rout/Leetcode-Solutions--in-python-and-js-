/*
Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.

Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
 
Constraints:
1 <= a, b <= 1000
*/

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var commonFactors = function (a, b) {
    let aFactors = [];
    for (let i = 1; i < a + 1; i++) {
        let divisor = i;
        if (a % divisor == 0) {
            aFactors.push(i);
        }
    }

    let bFactors = [];
    for (let i = 1; i < b + 1; i++) {
        let divisor = i;
        if (b % divisor == 0) {
            bFactors.push(i);
        }
    }

    let result = 0;
    for (let i = 0; i < aFactors.length; i++) {
        for (let j = 0; j < bFactors.length; j++) {
            if (aFactors[i] == bFactors[j]) {
                result += 1;
            }
        }
    }
    return result;
};

let a = 25;
let b = 30;
console.log(commonFactors(a, b));