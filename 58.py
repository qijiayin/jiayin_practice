#58 length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 :
            return 0
        i = len(s) - 1

        while i>=0 and s[i] == ' ':
            i -= 1

        end = i

        while i>=0 and s[i] != ' ':
            i -= 1

        return end - i
