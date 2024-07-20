/*
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
    let nums1Len = nums1.length;
    let nums2Len = nums2.length;
    if (nums1Len < nums2Len) {
        shorterArr = nums1;
        longerArr = nums2;
    } else {
        shorterArr = nums2;
        longerArr = nums1;
    }

    let result = [];
    // The usedIndices set ensures that each index of longerArr is only used once.
    let usedIndices = new Set();

    for (let i = 0; i < shorterArr.length; i++) {
        for (let j = 0; j < longerArr.length; j++) {
            if (shorterArr[i] == longerArr[j] && !usedIndices.has(j)) {
                result.push(shorterArr[i]);
                usedIndices.add(j);
                break;
            }
        }
    }

    return result;
};

let nums1 = [4, 9, 5];
let nums2 = [9, 4, 9, 8, 4];
console.log(intersect(nums1, nums2));