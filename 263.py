#263 ugly-number/
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 : return False
        if num == 1 : return True
        ugly_list=[2,3,5]
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 : return False
        for x in ugly_list :
            if num % x == 0:
                return self.isUgly(num / x )
