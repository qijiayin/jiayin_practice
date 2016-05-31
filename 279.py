#279 perfect-squares/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """


        res=[0 for i in range(n+1)]
        for i in range(1, n/2 + 2):
            if i * i > n :
                continue
            res[i*i] = 1

        for i in range(n+1):
            if res[i] == 1:
                continue
            cur = res[1] + res[i-1]
            for j in range(2, i):
                cur = min(cur, res[j] + res[i-j])
            res[i] = cur

        return res[n]
