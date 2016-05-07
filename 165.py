#165 compare-version-numbers/
class Solution(object):
    def getVal(self, l, idx):
        if idx < 0 or idx >= len(l):
            return 0
        else:
            return int(l[idx])

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))

        for i in range(n):
            x = self.getVal(v1, i)
            y = self.getVal(v2, i)
            if x > y:
                return 1
            if x == y:
                continue
            else:
                return -1


        return 0
