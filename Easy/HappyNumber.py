class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_str = str(n)
        dict = {}
        sum = 0
        counter = 0

        while sum != 1:
            # print "sum: ", sum
            if counter != 0: 
                n_str = str(sum)
            counter += 1
            sum = 0;
            for digit in n_str:
                sum += int(digit)* int(digit)
            if n_str in dict: 
                return False
            else:
                dict[n_str] = sum

        # print "hi"
        return True
