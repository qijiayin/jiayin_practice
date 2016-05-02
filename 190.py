#190 reverse-bits/
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(0, 32) :
            res <<= 1
            res += (n & 1)
            n >>= 1
        return res
