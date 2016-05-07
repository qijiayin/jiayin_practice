#168 excel-sheet-column-title/
class Solution(object):


    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        case : 26
        """

        res = ""
        while n > 0 :

            res = chr((n - 1) % 26  + ord('A')) + res
            n = (n - 1) / 26
        return res
        
