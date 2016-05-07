#303 range-sum-query-immutable/
class NumArray(object):
    def getTotleSum(self, nums):
        res = 0
        for i in range(len(nums)):
            res += nums[i]
        return res

    def getBeginSum(self,nums):
        res = []
        if len(nums) == 0 :
            return res
        res.append(nums[0])
        for i in range(1, len(nums)):
            res.append(res[i-1] + nums[i])
        print res
        return res

    def getEndSum(self,nums):
        res = []
        if len(nums) == 0 :
            return res
        res.append(nums[-1])
        for i in range(len(nums) - 2 , 0):
            res.append(res[i + 1] + nums[i])
        print res
        return res


    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.totle_sum = self.getTotleSum(nums)
        self.from_begin_sum = self.getBeginSum(nums)
        self.from_end_sum = self.getEndSum(nums)



    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.totle_sum - self.from_begin_sum[i] - self.from_end_sum[j]


# Your NumArray object will be instantiated and called as such:
nums = [[-2,0,3,-5,2,-1]]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
