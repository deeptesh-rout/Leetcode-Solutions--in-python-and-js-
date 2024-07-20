/*
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

*/

var largestNumber = function (nums) {
    if (nums.every(num => num === 0)) {
        return "0";
    }
    nums.sort(function (a, b) {
        return ("" + b + a) - ("" + a + b);
    });
    return nums.join('');
};

var nums = [3, 30, 34, 5, 9];
console.log(largestNumber(nums));



