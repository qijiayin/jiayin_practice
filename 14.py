#14 ongest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = ""
        if len(strs) == 0 :
            return LCP
        if len(strs) == 1:
            return strs[0]


        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if len(strs[j]) <= i:
                    return LCP
                if strs[j][i] != strs[0][i]:
                    return LCP
            LCP += strs[0][i]

        return LCP
