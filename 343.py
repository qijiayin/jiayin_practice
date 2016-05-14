#343 integer-break/
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1 :
            return 0

        product = [i for i in range(n+1)]
        product[n] = 0
        for x in  range(1, n ):
            for y in range(1, x+1):
                m = x + y
                if m > n :
                    continue
                product[m] = max( product[m], product[x] * product[y])
                print x,y,product[m], product[x] * product[y]
        return product[n]
