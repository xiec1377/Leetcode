class Solution {
public:
    bool isValid(string s) {
        vector<char> left;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                left.push_back(s[i]);
            } else if (!left.empty()) {
                if (s[i] == ')' && left.back() == '(') {
                    left.pop_back();
                } else if (s[i] == ']' && left.back() == '[') {
                     left.pop_back();
                } else if (s[i] == '}' && left.back() == '{') {
                     left.pop_back();
                } else { return false; }
            } else {
                return false;
            }
        }
        if (left.empty()) {
            return true;
        } else {
            return false;
        }
    }
};
