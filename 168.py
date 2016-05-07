#168 excel-sheet-column-title/
class Solution(object):
    def getChar(self, val):
        if val == 0 :
            return ''

        return chr(val - 1  + ord('A'))

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        case : 26
        """

        res = ""
        while n > 0 :
            val = n % 26
            res += self.getChar(val)
            n /= 26

        return res[::-1]
