#153 find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg = 0
        end = len(nums) - 1
        while beg <= end:
            mid = (beg+end) / 2
            if nums[beg] <= nums[end] :
                return nums[beg]
            else:
                if nums[mid] >= nums[end]:
                    beg = mid + 1
                else:
                    end = mid
        return beg
