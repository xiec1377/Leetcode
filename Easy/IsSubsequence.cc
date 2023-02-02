class Solution {
public:
    bool isSubsequence(string s, string t) {
        list<char> ss;
        list<char> tt;
        int tt_size = 0;
        for (int i = 0; i < s.length(); i++) {
            ss.push_back(s[i]);
        }
        for (int j = 0; j < t.length(); j++) {
            tt.push_back(t[j]);
        }
        //cout << "size: " << tt.size() << endl;
        tt_size = tt.size();
        for (int i = 0; i < tt_size; i++) {
            //cout << "i: " << i << endl;
            if (tt.front() == ss.front()) {
                tt.pop_front();
                ss.pop_front();
            } else {
                tt.pop_front();
            } 
        }
        /*for (auto const &x : ss) {
            cout << x << endl;
        }
        cout << "////" << endl;
        for (auto const &x : tt) {
            cout << x << endl;
        }*/
        
        if (ss.size() != 0 && tt.size() == 0) {
            return false;
        } else {
            return true;
        }
    }
};
