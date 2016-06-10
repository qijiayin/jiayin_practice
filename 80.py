#remove-duplicates-from-sorted-array-ii/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        end = 0
        cur = end + 1
        count = 1
        while cur < len(nums):
            if nums[cur] == nums[end]:
                count += 1
            else:
                count = 1

            if count <= 2:
                end += 1
                nums[end] = nums[cur]
            cur += 1
        return end+1
