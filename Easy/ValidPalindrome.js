/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let t = "";
    for (let i = 0; i < s.length; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            t += s[i].toLowerCase();
        } else if ((s[i] >= 'a' && s[i] <= 'z') ||
        s[i] >= '0' && s[i] <= '9') {
            t += s[i];
        }
    }
    //console.log("t:" + t);
    let half = 0;
    for (let i = 0; i < t.length; i++) {
        if (t[i] != t[t.length - 1 - i]) {
            return false;
        }
    }
    return true;
};
