/*
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 
Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
    let runningSum = [];
    runningSum.push(nums[0]);
    let store = 0;
    for (let i = 0; i < (nums.length - 1); i++) {
        store += nums[i];
        let sumNums = store + nums[i + 1];
        runningSum.push(sumNums);
    }
    return runningSum;
};

let nums = [3, 1, 2, 10, 1];
console.log(runningSum(nums));