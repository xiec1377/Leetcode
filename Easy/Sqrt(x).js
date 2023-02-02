/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    for (let i = 0; i <= x; i++) {
        //console.log(i + " "+ x);
        if (i * i == x) {
            //console.log("i: " + i);
            return i;
        } else if (i * i > x) {
            i--;
            //console.log("iii: " + i);
            return i;
        } 
    }
};
