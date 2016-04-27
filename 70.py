#70 climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        f_0 = 1
        f_1 = 2
        for i in range(3, n+1):
            f_2 = f_0 + f_1
            f_0 = f_1
            f_1 = f_2
        return f_2
