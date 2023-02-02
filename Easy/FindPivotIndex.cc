class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int pivot = 0;
        int pivoti = 0;
        int rightSum = 0;
        int leftSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            pivoti = i;
            leftSum += nums[i];
            for (int j = pivoti + 1; j < nums.size(); j++) {
                rightSum += nums[j];
            }
            //cout << "sums: " << leftSum-nums[pivoti] << " & " << rightSum << endl;
            //leftSum -= nums[pivoti];
            if (leftSum-nums[pivoti] == rightSum) {
                return pivoti;
            }
            rightSum = 0;
        }
        return -1;
    }
};
