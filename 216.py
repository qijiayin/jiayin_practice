# 216 combination-sum-iii/
class Solution(object):
    def sum3(self, res, cur_res, idx, k, n, num):
        if idx >k or n < 0 :
            return []
        if idx == k and n > 0 :
            return []
        if idx == k and n == 0:
            res.append(cur_res)
            return res
        cur_res[idx] = num
        for i in range(num+1, 10):
            l = self.sum3(res, cur_res, idx+1,  k , n-num, i)
            if len(l) > 0 :
                res.append(l)
        return res

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        cur_res = [0 for i in range(k) ]
        for i in range(1, 10):
            l = self.sum3(res, cur_res,0,  k, n, i)
            if len(l) > 0 :
                res.append(l)
        return res

s=Solution()
res = s.combinationSum3(3,9)
print res
