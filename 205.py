#205 isomorphic-strings/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        case: ab , aa
        """

        if len(s) != len(t) :
            return False
        flag = [False for i in range(0,256) ]
        cmap = {}
        for i in range(0, len(s)):

            if s[i] in cmap.keys() :
                if cmap[s[i]] != t[i]:
                    return False
            else:
                idx = ord(t[i])
                if flag[idx] == True :
                    return False
                cmap[s[i]] = t[i]
                flag[idx] = True
        return True
