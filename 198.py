#198 house-robber/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 : return 0
        if len(nums) == 1 : return nums[0]
        if len(nums) == 2 : return max(nums[0], nums[1])
        f_0 = nums[0]
        f_1 = max(nums[0], nums[1])
        for i in range(2, len(nums)) :
            f_2 = max(f_0 + nums[i], f_1 )
            f_0 = f_1
            f_1 = f_2

        return f_2
