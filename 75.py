#75 sort-colors/
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1 :
            return
        red = -1
        i = 0
        blue = len(nums)
        while i < blue :
            val = nums[i]
            if val == 0 :
                red += 1
                tmp = nums[red]
                nums[red] = nums[i]
                nums[i] = tmp
                i += 1

            if val == 1:
                i += 1
            if val == 2:
                blue -= 1
                tmp = nums[blue]
                nums[blue] = nums[i]
                nums[i] = tmp
