#268 missing-number/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = sum_expect = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            sum_expect += i
        sum_expect += len(nums)
        return sum_expect - sum
