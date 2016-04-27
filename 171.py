#171-excel-sheet-column-number
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        for i in range(0,len(s)):
            num *= 26
            num += (ord(s[i].upper())-ord('A')+1)
        return num
