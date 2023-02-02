#include <string>

class Solution {
public:
    vector<string> words;
    string split(string s, char delim) {
        string t;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == delim) {
                t += "";
                if (t.length() != 0) {
                    words.push_back(t);
                }
                
                //cout << "t: " << t << endl;
                t = "";
            } else {
                t += s[i];
                if (i == s.length()-1) {
                    words.push_back(t);
                }
            }
        }
        return t;
    }
    int lengthOfLastWord(string s) {
        string t;
        split(s, ' ');
        //cout << words.back().length() << endl;
        return words.back().length();
    }
};
