#39 combination-sum/
class Solution(object):
    def combinImp(self,candidates, target, cur_sum, res, cur, idx):
        n = len(candidates)
        if idx >= n:
            if target == cur_sum :
                combine = []
                for i in range(0, n):
                    for j in range(0,cur[i]) :
                        combine.append(candidates[i])
                res.append(combine)
            return

        val = candidates[idx]
        cnt = 0
        while cur_sum + cnt*val <= target :
            cur[idx] = cnt
            self.combinImp(candidates, target, cur_sum + cnt * val, res,  cur, idx+1)
            cnt += 1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        cur = [0 for i in candidates]
        self.combinImp(candidates, target, 0, res, cur, 0)
        return res
