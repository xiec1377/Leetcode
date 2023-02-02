class Solution {
public:
    bool isVowel(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            return true;
        } else {
            return false;
        }
    }
    
    string reverseVowels(string s) {
        vector<char> vowels;
        string output;
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(tolower(s[i]))) {
                vowels.push_back(s[i]);
            }
        }
        for (int j = 0; j < s.length(); j++) {
            if (!isVowel(tolower(s[j]))) {
                output += s[j];
            } else {
                output += vowels.back();
                vowels.pop_back();
            }
        }
        return output;
    }
};
