#include <string>

class Solution {
public:
    string intToRoman(int num) {
        string roman;   // output
        string numStr;  // num input to string
        string first;
        int i = 0;  // loop counter
        numStr = to_string(num);
        int forCounter = 0;
        
        while (numStr[0] != '\0') { //for (int j = 0; j < numStr.length(); j++) {
            if (numStr.length() == 4) {
                first.clear();
                first.push_back(numStr[0]);
                forCounter = stoi(first);
                for (int i = 0; i < forCounter; i++) {
                    roman.append("M");
                }
                numStr.erase(0, 1);     // pop first char of numStr
            } else if (numStr.length() == 3) {
                first.clear();
                first.push_back(numStr[0]);
                forCounter = stoi(first);
                if (numStr[0] == '9') {
                    roman.append("CM");
                } else if (numStr[0] == '4') {
                    roman.append("CD");
                } else if (numStr[0] == '5') {
                    roman.append("D");
                } else if (numStr[0] > '5' && numStr[0] < '9') {
                    roman.append("D");
                    for (int i = 0; i < forCounter - 5; i++) {
                        roman.append("C");
                    }
                } else {
                    for (int i = 0; i < forCounter; i++) {
                        roman.append("C");
                    }
                }
                numStr.erase(0, 1);
            } else if (numStr.length() == 2) {
                first.clear();
                first.push_back(numStr[0]);
                forCounter = stoi(first);
                if (numStr[0] == '4') {
                    roman.append("XL");
                } else if (numStr[0] == '9') {
                    roman.append("XC");
                } else if (numStr[0] == '5') {
                    roman.append("L");
                } else if (numStr[0] > '5' && numStr[0] < '9') {
                    roman.append("L");
                    for (int i = 0; i < forCounter - 5; i++) {
                        roman.append("X");
                    }
                } else {
                    for (int i = 0; i < forCounter; i++) {
                        roman.append("X");
                    }
                }
                numStr.erase(0, 1);
            } else if (numStr.length() == 1) {
                first.clear();
                first.push_back(numStr[0]);
                forCounter = stoi(first);
                if (numStr[0] == '4') {
                    roman.append("IV");
                } else if (numStr[0] == '9') {
                    roman.append("IX");
                } else if (numStr[0] == '5') {
                    roman.append("V");
                } else if (numStr[0] > '5' && numStr[0] < '9') {
                    roman.append("V");
                    for (int i = 0; i < forCounter - 5; i++) {
                        roman.append("I");
                    }
                } else {
                    for (int i = 0; i < forCounter; i++) {
                        roman.append("I");
                    }
                    
                }
                numStr.erase(0, 1);
            }
        }
        return roman;
    }
};
