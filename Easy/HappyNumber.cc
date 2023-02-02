#include <string>

class Solution {
public:
    bool isHappy(int n) {
        vector<int> digits;
        vector<int> sums;
        string n_str;
        int digit;
        int sum;
        int m = n;
        bool looping = true;
        while (looping) {
            n_str = to_string(m);
            sum = 0;
            for (int i = 0; i < n_str.length(); i++) {
                digit = int(n_str[i]) - 48;
                //cout << "digit: " << digit << endl;
                digits.push_back(digit);
            }
            for (int i = 0; i < digits.size(); i++) {
                //cout << "VECTOR- --->" << endl;
                //cout << digits[i] << endl;
                sum += digits[i] * digits[i];
            }
                
            //cout << "Sum: " << sum << endl;

            if (sum == 1) {
                return true;
            } else if (find(sums.begin(), sums.end(), sum) != sums.end()){
                // sum found in sums vector
                return false;
            } else {
                sums.push_back(sum);
                looping = true;
            }
            digits.clear();
            m = sum;
        }
        return false;
    }
};
