/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let res = nums.filter(i => i != val);
    for (let i = 0; i < res.length; i++) {
        nums[i] = res[i];
        //console.log(res[i]);
    }
    return res.length;
};
