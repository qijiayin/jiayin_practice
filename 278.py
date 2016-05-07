#278 first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def find(self, beg, end, fstbad):
        if beg > end :
            return fstbad
        mid = (beg + end ) / 2
        if isBadVersion(mid) == True :
            fstbad = min(mid, fstbad)
            return self.find(beg, mid - 1, fstbad)
        else :
            return self.find(mid + 1, end, fstbad)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.find(1, n, n)
