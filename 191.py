# 191 number-of-1-bits/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 0:
            x = n & 1
            if x % 2 == 1 :
                num += 1
            n >>= 1

        return num

s=Solution()
print s.hammingWeight(1)
