#303 range-sum-query-immutable/
class NumArray(object):


    def getSumList(self,nums):
        res = []
        if len(nums) == 0 :
            return res
        res.append(nums[0])
        for i in range(1, len(nums)):
            res.append(res[i-1] + nums[i])
        return res



    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sumlist = []
        self.sumlist = self.getSumList(nums)




    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return  self.sumlist(j) -  self.sumlist(i-1)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
