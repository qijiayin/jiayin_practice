#7 reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 :
            return 0
        if x < 0:
            flag = -1
            x *= -1
        else :
            flag = 1
        MAXINT = 2147483648
        res = 0
        while x > 0 :
            res *= 10
            res += (x % 10)
            x /= 10
        return res * flag
