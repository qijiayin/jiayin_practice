#118 pascals-triangle/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        preList = []
        for n in range(1, numRows+1) :
            curList = []
            curList.append(1)
            for i in range(1, n-1):
                curList.append(preList[i] + preList[i-1])
            if n > 1 : curList.append(1)
            preList = curList
            res.append(curList)
        return res
