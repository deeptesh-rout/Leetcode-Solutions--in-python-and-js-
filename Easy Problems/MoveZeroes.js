/*
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
    const noZeros = nums.filter(num => num != 0);
    let allZeros = [];
    for (let num of nums) {
        if (num == 0) {
            allZeros.push(num)
        }
    }
    // Clear the original array.
    nums.length = 0;

    // Concatenate noZeros and allZeros back into nums.
    nums.push(...noZeros, ...allZeros);
};

let nums = [0, 1, 0, 3, 12];
console.log(moveZeroes(nums));