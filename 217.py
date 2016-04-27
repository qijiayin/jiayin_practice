# 217  contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for x in nums:
            if d.has_key(x): return True
            d[x]=''

        return False
