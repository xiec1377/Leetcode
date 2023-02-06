/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let diff = 0;
    const output = new Array(2);
    for (let i = 0; i < nums.length; i++) {
        diff = target - nums[i];
        output[0] = i;
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] == diff) {
                output[1] = j;
                return output;
            }
        }
    }
};
