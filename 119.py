#119 pascals-triangle-ii/
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0 : return [1]
        pre_line = [1]
        for i in range(1, rowIndex + 1 ):
            cur_line = []
            cur_line.append(1)
            for j in range(1, i):
                #print len(pre_line), j
                cur_line.append(pre_line[j] + pre_line[j-1])
            cur_line.append(1)
            pre_line = cur_line

        return pre_line
