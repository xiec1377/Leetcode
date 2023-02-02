class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        int i = 0;
        bool pal;
        if (s[0] == '-') {      // negative integer
            return false;
        }
        if (s.length() % 2 == 0) {
            if (s.length() == 2) { 
                if (s[0] == s[1]) {
                    return true;
                } else {
                    return false;
                }
            }
            i = (s.length() / 2) - 1;
            for (int j = i; j >= 0; j--) {
                    //cout << s[j] << " & " << s[s.length() - j] << endl;
                    //cout << j << " & " << s.length() - j << endl;
                if (s[j] == s[s.length() - 1 - j]) {
                        pal = true;
                    } else {
                        pal = false;
                        break;
                    }
                
            }
        } else {
            if (s.length() == 1) {
                return true;
            } else if (s.length() == 3) {
                i = s.length() / 2;
                if (s[i-1] == s[i+1]) {
                    return true;
                } else {
                    return false;
                }
            }   
            i = (s.length() / 2) + 1;
            cout << "i: " << i << endl;
            for (int j = i - 1; j >= 0; j--) {
                for (int k = i + 1; k < s.length(); k++) {
                    if (s[j] == s[k]) {
                        pal = true;
                    } else {
                        pal = false;
                        break;
                    }
                }
            }
        }
        if (pal) {
            return true;
        } else {
            return false;
        }
    }
};
