#66 plus-one/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(0, len(digits)):
            num *= 10
            num += digits[i]
        num += 1
        res = []
        while num > 0:
            res.append( num % 10 )
            num /= 10

        res.reverse()
        return res
