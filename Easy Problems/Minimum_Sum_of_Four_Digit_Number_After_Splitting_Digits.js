/*
You are given a positive integer num consisting of exactly four digits. 
Split num into two new integers new1 and new2 by using the digits found in num. 
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. 
Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

Example 1:
Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.

Example 2:
Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
 
Constraints:
1000 <= num <= 9999
*/

/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function (num) {
    let numStr = num.toString();

    let splittedNum = numStr.split("");

    let minDigit1 = Math.min(...splittedNum);
    splittedNum.splice(splittedNum.indexOf(minDigit1.toString()), 1);

    let minDigit2 = Math.min(...splittedNum);
    splittedNum.splice(splittedNum.indexOf(minDigit2.toString()), 1);

    let maxDigit1 = Math.max(...splittedNum);
    splittedNum.splice(splittedNum.indexOf(maxDigit1.toString()), 1);

    let maxDigit2 = Math.max(...splittedNum);
    splittedNum.splice(splittedNum.indexOf(maxDigit2.toString()), 1);

    let num1 = "";
    num1 += minDigit1;
    num1 += maxDigit1;

    let num2 = "";
    num2 += minDigit2;
    num2 += maxDigit2;

    let result = parseInt(num1) + parseInt(num2);

    return result;
};

let num = 2932;
console.log(minimumSum(num));