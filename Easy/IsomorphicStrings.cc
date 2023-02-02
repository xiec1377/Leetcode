class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> m;
        if (s.length() == t.length()) {
            for (int i = 0; i < s.length(); ++i) {
                if (m.find(s[i]) == m.end()) {  // key not found
                    for (auto const x : m) {
                        if (x.first != s[i] && x.second == t[i]) {
                            return false;
                        }
                    }
                    m[s[i]] = t[i];
                } else if (m[s[i]] != t[i]) {
                    return false;
                }
            }
        } else {
            return false;
        }
        return true;
    }
};
