/*
Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function (nums) {
    let count = {};
    for (i = 0; i < nums.length; i++) {
        if (nums[i] % 2 == 0) {
            if (nums[i] in count) {
                count[nums[i]] += 1;
            }
            else {
                count[nums[i]] = 1;
            }
        }
    }
    if (!Object.keys(count).length) {
        return -1;
    }
    let max_value = Math.max(...Object.values(count));
    let most_frequent_even = [];
    for (let key in count) {
        if (count[key] == max_value) {
            most_frequent_even.push(key);
        }
    }
    return Math.min(...most_frequent_even);
};


let nums = [4, 4, 4, 9, 2, 4];
console.log(mostFrequentEven(nums));