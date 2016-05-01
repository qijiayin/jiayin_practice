#9 palindrome-number/ 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        name : ndigits, msb, val
        """
        if x < 0 :
             return False


        msb = 1
        n = x
        while n >= 10:
            msb *= 10
            n /= 10
        #print base
        while x > 0 :
            if (x / msb) != (x % 10) :
                return False
            x -= (x / msb * msb)
            x /= 10
            msb /= 100
        return True
