#38 count-and-say/ 写错了好多次，有没有秘诀啊
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1 : return "1"
        s = "1"
        for k in range( 2, n + 1 ):
            next_s = ""
            pre_c = ""
            for i in range(len(s)) :
                cur_c = s[i]
                if pre_c == "":
                    pre_c = cur_c
                    cnt = 1
                elif pre_c == cur_c :
                    cnt += 1
                else :
                    next_s += (str(cnt) + pre_c)
                    pre_c = cur_c
                    cnt = 1
            next_s += (str(cnt) + pre_c)
            s = next_s

        return s
