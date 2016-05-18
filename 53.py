# 53 maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1 :
            return 0
        max_sum = nums[0]
        f_0 = nums[0]
        f_1 = 0
        for i in range(1, len(nums)):
            f_1 = max(f_0 + nums[i], nums[i])
            max_sum = max(max_sum, f_1)
            f_0 = f_1

        return max_sum
