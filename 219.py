#219 contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ndict = {}
        for i in range(0, len(nums)) :
            if nums[i] not in ndict.keys() :
                ndict[nums[i]] = i
            else:
                idx = ndict[nums[i]]
                if i - idx <= k :
                    return True
                else:
                    ndict[nums[i]] = i
        return False
