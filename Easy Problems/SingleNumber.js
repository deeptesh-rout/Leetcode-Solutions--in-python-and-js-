/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber1 = function (nums) {
    let count = {};
    for (let num of nums) {
        if (num in count) {
            count[num] += 1;
        } else {
            count[num] = 1;
        }
    }
    for (let key in count) {
        if (count[key] == 1) {
            return parseInt(key);
        }
    }
};

let nums = [4, 1, 2, 1, 2];
console.log(singleNumber1(nums));


/**
 * @param {number[]} nums2
 * @return {number}
 */
var singleNumber2 = function (nums2) {
    nums2.sort();
    for (let i = 0; i < nums2.length - 1; i += 2) {
        if (nums2[i] != nums2[i + 1]) {
            return nums2[i];
        }
    }
    return nums2[nums2.length - 1];
};

let nums2 = [4, 1, 2, 1, 2];
console.log(singleNumber2(nums2));