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
            return str == ""
        ptn_map_str = {}
        str_map_ptn = {}

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

            if p not in ptn_map_str.keys() :
                ptn_map_str[p] = s

            elif s != ptn_map_str[p] :
                return False

            if s not in str_map_ptn.keys():
                str_map_ptn[s] = p
            elif p != str_map_ptn[s] :
                return False

        return beg == len(str)
