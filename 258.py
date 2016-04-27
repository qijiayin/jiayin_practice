#258 add-digits
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10 : return num
        else:
            new_num=0
            while num>0 :
                new_num += num % 10
                num /= 10
            return self.addDigits(new_num)
