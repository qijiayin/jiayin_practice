#290 word-pattern/
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        case : "abba"
        "dog dog dog dog"
        false
        """
        if str == "" :
            return pattern == ""
        if pattern == "":
            return True
        strmap = {}
        beg = 0
        end = 0
        for p in pattern :
            while beg < len(str) and str[beg] == ' ':
                beg += 1
            end = beg
            while end < len(str) and str[end] != ' ':
                end += 1
            s = str[beg:end]
            beg = end
            if s == "" :
                return False
            print s,p
            if p not in strmap.keys() :
                strmap[p] = s
            elif s != strmap[p] :
                return False
        return beg == len(str)
