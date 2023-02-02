class Solution {
public:
    int romanToInt(string s) {
        int i = 0; // counter
        int j = 0;  // result
        bool isSubtract = false; 
        while (s[i] != '\0') {
            if (s[i] == 'M') {
                j += 1000;
                i++;
            } else if (s[i] == 'D') {
                j += 500;
                i++;
            } else if (s[i] == 'C') {
                if (s[i+1] == 'D') {
                    j += 400;
                    i += 2;
                } else if (s[i+1] == 'M') {
                    j += 900;
                    i += 2;
                } else {
                    j += 100;
                    i++;
                }
            } else if (s[i] == 'L') {
                j += 50;
                i++;
            } else if (s[i] == 'X') {
                if (s[i+1] == 'L') {
                    j += 40;
                    i += 2;
                } else if (s[i+1] == 'C') {
                    j += 90; 
                    i += 2;
                } else {
                    j += 10; 
                    i++;
                }
            } else if (s[i] == 'V'){
                j += 5;
                i++;
                if (s[i+1] == 'I') {
                    isSubtract = true;
                }
            } else if (s[i] == 'I') {
                if (s[i+1] == 'V') {
                    j += 4;
                    i += 2;
                } else if (s[i+1] == 'X') {
                    j += 9;
                    i += 2;
                } else {
                    j++;
                    i++;
                }
            }
        }
        return j;
    }
};
