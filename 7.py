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
        MAXINT = 2**31 -1
        MININT = 2**31 * -1

        res = 0
        while x > 0 :
            if res == MAXINT / 10:
                if (flag > 0 and (x % 10) > 7 ) or (flag < 0 and (x % 10) > 8):
                    return 0

            elif res > MAXINT / 10:
                return 0

            res *= 10
            res += (x % 10)
            x /= 10
            print x

        return res * flag
