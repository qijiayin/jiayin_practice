#96 unique-binary-search-trees/
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=[1,1]
        for i in range(2, n+1):
            sum = 0
            for k in range(0, i):
                sum += (f[k] * f[i-k-1])
            f.append(sum)
        return f[n]
