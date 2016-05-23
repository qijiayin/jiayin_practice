#202 happy-number/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
        s = str(n)
        dict = {}
        x = 0

        while x != 1:
            x = 0
            for c in s :
                x += int(c) * int(c)
            if dict.get(x) != None:
                return False
            else:
                dict[x] = True
            s = str(x)
        return True
