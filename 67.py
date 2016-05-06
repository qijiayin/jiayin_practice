#67 add-binary/
class Solution(object):
    def getVal(self, string, i):
        if i >= len(string) or i <0 :
            return 0
        else:
            return (ord(string[i]) - ord('0'))
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res = ""
        i=len(a) - 1
        j=len(b) - 1
        carry = 0
        while i >= 0 or  j >= 0 :
            sum = carry + self.getVal(a,i) + self.getVal(b,j)
            add = sum % 2
            carry = sum / 2
            res += str(add)
            #print i,j, sum, res, self.getVal(a,i) , self.getVal(b,j)
            i -= 1
            j -= 1

        if carry > 0 :
            res += str(carry)


        return res[::-1]
