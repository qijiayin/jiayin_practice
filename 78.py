#78 subset
class Solution(object):
    def subsetImp(self, nums, res, cur, idx):
        if idx >= len(nums) :
            sub = []
            for i in range(0,len(cur)):
                if cur[i] == 1:
                    sub.append(nums[i])
            res.append(sub)
            return

        cur[idx] = 0
        self.subsetImp(nums, res, cur, idx+1)
        cur[idx] = 1
        self.subsetImp(nums, res, cur, idx+1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        cur = [0 for i in nums]
        self.subsetImp(nums, res, cur, 0)
        return res
