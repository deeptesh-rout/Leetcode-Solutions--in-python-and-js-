/*
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:
leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

Example 1:
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:
Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 105
*/

function sum(arr) {
    return arr.reduce((acc, val) => acc + val, 0);
}
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function (nums) {
    let leftSum = [];
    for (let i = 0; i < nums.length; i++) {
        if (i == 0) {
            leftSum.push(0);
        } else {
            leftSum.push(sum(nums.slice(0, i).reverse()));
        }
    }
    let numLength = nums.length;
    let rightSum = [];
    for (let i = 0; i < numLength; i++) {
        rightSum.push(sum(nums.slice(i + 1)));
    }
    let ans = [];
    for (let i = 0; i < numLength; i++) {
        let result = Math.abs(leftSum[i] - rightSum[i]);
        ans.push(result);
    }
    return ans;
};

let nums = [10, 4, 8, 3];
console.log(leftRightDifference(nums));