#213 house-robber-ii/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        nums.extend(nums)

        profit = [0 for i in range(2*n) ]
        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])

        for i in range(2, 2*n):
            profit[i] = max(profit[i-2] + nums[i],  profit[i-1])
        print profit
        return profit[2*n - 1] - profit[n-1]
