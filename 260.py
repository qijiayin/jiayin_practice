#260 ingle-number-iii/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res=[]
        if len(nums) == 1 :
            res.append(nums[0])
        if nums[0] != nums[1]:
            res.append(nums[0])
        if nums[len(nums)-1] != nums[len(nums) - 2] :
            res.append(nums[len(nums) -1 ])

        for i in range(1, len(nums) - 1):
            if len(res) == 2:
                return res
            if nums[i] != nums[i-1] and nums[i] !=nums[i+1] :
                res.append(nums[i])

        return res
