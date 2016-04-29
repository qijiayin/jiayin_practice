#26 remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [0,i-1] done
        [j,n-1] todo
        len : i+1
        """
        if len(nums) < 2 : return len(nums)
        i = 0
        for j in range(1, len(nums)) :
            if nums[j] != nums[i] :
                nums[i+1] = nums[j]
                i += 1

        return i+1
