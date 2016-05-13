#238 product-of-array-except-self/
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for i in range(len(nums))]
        from_begin_product = 1
        for i in range(1, len(nums)) :
            from_begin_product = from_begin_product * nums[i-1]
            res[i] = from_begin_product

        from_end_product = 1
        for i in range(len(nums)-2, -1 , -1) :
            from_end_product = from_end_product * nums[i+1]
            res[i] *= from_end_product

        return res
