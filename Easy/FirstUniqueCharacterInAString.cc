class Solution {
public:
    int firstUniqChar(string s) {
        map<char, pair<int, int>> freq;
        int index = s.length() - 1;
        bool allRepeat = true;
        for (int i = 0; i < s.length(); i++) {
            
            if (freq[s[i]].second >= 1) {
                freq[s[i]].second++;
            } else {
                freq[s[i]] = {i, 1};
            }
            
        }
        // iterate through map to find first non-repeating char
        for (auto const& x : freq) {
            //cout << x.first << " & " << x.second.first << ", " << x.second.second << endl;
            if (x.second.second == 1) {
                if (x.second.first <= index) {
                    index = x.second.first;
                    allRepeat = false;
                }
            }
        }
        if (allRepeat) {
            return -1;
        } else {
            return index;
        }
    }
};
