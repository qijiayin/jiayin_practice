#125 valid-palindrome/
class Solution(object):
    def isValidChar(self, c):
        if ( ord(c) >= ord('a') and ord(c) <= ord('z') ) or (ord(c) >= ord('0')  and ord(c) <= ord('9') )  :
            return True
        else :
            return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "" :
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i <= j :
            if self.isValidChar(s[i]) == False :
                i += 1
                continue
            if self.isValidChar(s[j]) == False :
                j -= 1
                continue
            if s[i] != s[j] :
                return False
            i += 1
            j -= 1
        return True
