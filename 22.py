#22 generate-parentheses/
class Solution(object):
    def genImp(self, res, cur_str, i, left_cnt, right_cnt):
        if i < 0 :
            res.append(cur_str)
            return res
        i -= 1
        if left_cnt > right_cnt :
            return res
        if left_cnt > 0:
            res = self.genImp(res, cur_str + "(" , i, left_cnt - 1,  right_cnt)
        if right_cnt > 0:
            res = self.genImp(res, cur_str + ")", i, left_cnt, right_cnt - 1)
        return res

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur_str = ""

        res = self.genImp(res, cur_str, 2*n - 1,  n, n)
        return res
