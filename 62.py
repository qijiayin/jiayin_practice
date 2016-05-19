#62 unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        path=[[0 for i in range(n)] for i in range(m)]
        for j in range(n) :
            path[0][j] = 1
        for i in range(m):
            path[i][0] = 1
        for j in range(1,n) :
            for i in range(1, m):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[m-1][n-1]
