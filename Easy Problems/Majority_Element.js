/*
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
    let count = {};
    let length = nums.length;
    for (i = 0; i < length; i++) {
        if (nums[i] in count) {
            count[nums[i]] += 1;
        }
        else {
            count[nums[i]] = 1;
        }
    }
    for (let key in count) {
        let value = count[key];  // Retrieve the value associated with the key.
        if (value > (length / 2)) {
            return parseInt(key);   // Convert key to integer.
        }
    }
};

nums = [2, 2, 1, 1, 1, 2, 2];
console.log(majorityElement(nums));