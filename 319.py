#319 bulb-switcher/
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [0 for i in range(n)]
        for i in range(1, n+1) :
            for j in range(n):
                if (j+1)%i == 0:
                    bulbs[j] ^= 1


        res = 0
        for i in range(n):
            if bulbs[i] == 1:
                res += 1
        return res
