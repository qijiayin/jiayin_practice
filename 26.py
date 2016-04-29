#26 remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [0, i-1] done
        [i, j-1] duplicate
        [j, n-1] todo
        """
        if len(nums) <= 1 : return len(nums)
        i = 0
        j = 1
        n = len(nums)
        while j < n :
            while j < n and nums[i] == nums[j]:
                j += 1
            idx = i + 1
            for k  in range(j, n):
                nums[idx] = nums[k]
                idx += 1

            n -= (j - i -1)
            i += 1
            j = i + 1

        return n
