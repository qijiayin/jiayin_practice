# 77 combinations/
class Solution(object):
    def combineImp(self, res, cur_res, cur_idx, k, i, n):
        if cur_idx == k:
            res.append([x for x in cur_res])
            print cur_res, res
            return
        if cur_idx > k:
            return

        for x in range(i, n+1):
            cur_res[cur_idx] = x
            self.combineImp(res, cur_res, cur_idx+1, k,  x+1, n)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n :
            return []
        res = []
        cur_res = [0 for i in range(k)]

        self.combineImp(res, cur_res, 0,  k, 1, n)
        return res
