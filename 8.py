#8 string-to-integer-atoi/
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        case : "    10" --- 10
        case:"        +0045" -- 45
        case : "  -0012a42" -- 12
        """
        if str == "":
            return 0
        res = 0
        idx = 0
        flag = 1
        while idx < len(str) and str[idx] == " ":
            idx += 1

        if str[idx] == '+' :
            flag = 1
            idx += 1
        elif str[idx] == '-':
            flag = -1
            idx += 1



        MAXINT = 2**31 - 1
        MININT = -1 * (2**31)
        while idx < len(str) :
            c = str[idx]

            if c < '0' or c > '9':
                return res * flag
            val = ord(c) - ord('0')
            if res  ==  MAXINT / 10 :
                if (flag > 0 and val > 7 ):
                    return MAXINT
                if (flag < 0 and val > 8) :
                    return MININT
            if res >  MAXINT / 10:
                if flag > 0 :
                    return MAXINT
                if flag < 0 :
                    return MININT
            else:
                res *= 10
                res += val
            idx += 1

        return res*flag
