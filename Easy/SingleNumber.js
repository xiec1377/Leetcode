/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    const map = new Map();
    let j = 0;
    for (let i = 0; i < nums.length; i++) {
        if (map.get(nums[i]) == false) {
            map.set(nums[i], true);   
        } else {
            map.set(nums[i], false);
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (map.get(nums[i]) == false) {
            return nums[i];
        }
    }
};
