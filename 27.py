# 27 remove-element/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        [0,i-1] done
        [i,j-1] todo
        [j,n-1] ==val
        """
        i = 0
        j = len(nums)
        while  i < j :
            if nums[i] == val :
                j -= 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            else:
                i += 1



        return j
