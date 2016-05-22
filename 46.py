#46 permutations/
class Solution(object):
    def perImp(self, res, cur_res, nums, select, idx):
        if idx == len(cur_res):
            res.append([x for x in cur_res])
            return
        if idx > len(cur_res):
            return
        for i in range(len(nums)):
            if select[i] == False:
                select[i] = True
                cur_res[idx] = nums[i]
                self.perImp(res, cur_res, nums, select, idx+1)
                select[i] = False


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        select =[False for x in nums]
        res = []
        cur_res = [0 for x in nums ]
        self.perImp(res, cur_res, nums, select, 0)
        return res
