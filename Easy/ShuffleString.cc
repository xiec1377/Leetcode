class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        map<int, char> dic;
        string t;
        for (int i = 0; i < s.length(); i++) {
            dic.insert({indices[i], s[i]});
        }
        for (int i = 0; i < indices.size(); i++) {
            auto itr = dic.find(i);
            //cout << itr->second << endl;
            t += itr->second;
        }
        return t;
    }
};
