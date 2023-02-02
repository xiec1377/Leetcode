class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output;
        int diff;
        for (int i = 0; i < nums.size(); ++i) {
            diff = target - nums[i];
            for (int j = i + 1; j < nums.size(); ++j) {
                if (diff == nums[j]) {
                    output.push_back(i);
                    output.push_back(j);
                }
            }
        }
        return output;
    }
};
