#342 power-of-four/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0  : return False
        if num == 1 : return True
        foundOneFlag = False
        while num > 0:

            if num == 1 : return True
            if  num & 2 or num & 1: return False
            num >>= 2


        return True
