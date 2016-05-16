#35 search-insert-position/
class Solution(object):
    def search(self, nums, target, beg, end):
        if beg > end :
            return beg
        mid = (beg + end) / 2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            return self.search(nums, target, mid+1, end)
        else:
            return self.search(nums, target, beg, mid-1)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search(nums, target, 0, len(nums) - 1)
