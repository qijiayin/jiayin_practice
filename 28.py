#28 implement-strstr/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" :
            return 0
        if haystack == "":
            return -1
        m = len(haystack)
        n = len(needle)

        beg = 0
        while m - beg >= n :
            if haystack[beg : beg + n] == needle :
                return beg
            beg += 1
        return -1
