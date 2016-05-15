#137 single-number-ii/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mask = 1
        for i in range(31):
            sum = 0
            for x in nums:
                sum += (x & mask)
            if sum % 3 != 0:
                res |= mask
            mask <<= 1
            print res, mask
        return res
